import pytest_asyncio
from fastapi.testclient import TestClient
from social_network_simulation.app import app
from sqlalchemy.ext.asyncio import create_async_engine
from social_network_simulation.core.database import (
    get_session,
    create_all,
    drop_all,
    async_sessionmaker,
)
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from social_network_simulation.models.user_model import UserModel
from datetime import datetime
from sqlalchemy import select


class Context:
    TEST_DB_DSN = "sqlite+aiosqlite:///test.db"
    client: TestClient
    session: AsyncSession
    engine: AsyncEngine

    async def __aenter__(self):
        self.engine = create_async_engine(self.TEST_DB_DSN)

        async with self.engine.begin() as conn:
            await create_all(conn)

        self.session = self.__get_session(self.engine)

        self.client = TestClient(app).__enter__()

        async def get_session_overrides():
            yield self.session

        app.dependency_overrides[get_session] = get_session_overrides

        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

        async with self.engine.begin() as conn:
            await drop_all(conn)

        self.client.__exit__()

        app.dependency_overrides.clear()

    async def new_user(self, user: dict):
        usr = UserModel(
            name=user["name"],
            username=user["username"],
            password=user["password"],
            birthday=datetime.strptime(user["birthday"], "%Y-%m-%d"),
            sex=user["sex"],
        )
        self.session.add(usr)
        await self.session.commit()
        await self.session.refresh(usr)
        return usr

    async def get_list_users(self):
        query = select(UserModel)
        result = await self.session.execute(query)
        all_users = result.scalars().all()
        return all_users

    def __get_session(self, engine):
        Session = async_sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
            class_=AsyncSession,
        )
        session: AsyncSession = Session()
        return session


@pytest_asyncio.fixture
async def context():
    async with Context() as ctx:
        yield ctx
