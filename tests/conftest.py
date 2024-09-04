import pytest_asyncio
from fastapi.testclient import TestClient
from social_network_simulation.app import app
from sqlalchemy.ext.asyncio import create_async_engine
from social_network_simulation.core.database import (
    generate_get_session,
    get_session,
    create_all,
    drop_all,
)
from sqlalchemy.ext.asyncio import AsyncSession
from social_network_simulation.models.user_model import UserModel
from datetime import date


@pytest_asyncio.fixture
async def client(session: AsyncSession):
    async def get_session_overrides():
        async for s in session:
            yield s

    with TestClient(app) as api_client:
        app.dependency_overrides[get_session] = get_session_overrides
        yield api_client

    app.dependency_overrides.clear()


@pytest_asyncio.fixture(scope="session")
async def engine():
    sqlite = "sqlite+aiosqlite:///database.db"
    _engine = create_async_engine(sqlite)
    async with _engine.begin() as conn:
        yield conn


@pytest_asyncio.fixture
async def user(session: AsyncSession):
    # async for s in session:
    user = UserModel(
        name="Nome1",
        username="Username1",
        password="12345678",
        birthday=date(1998, 2, 25),
        sex="outro",
    )
    async for s in session:
        s.add(user)
        await s.commit()
        await s.refresh(user)
        yield user
    else:
        raise Exception("Não foi!")


@pytest_asyncio.fixture
async def session(engine):
    await create_all(engine)

    get_session = generate_get_session(engine)
    session: AsyncSession = get_session()
    yield session
    await drop_all(engine)
