from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker as _async_sessionmaker,
    AsyncSession,
)
from social_network_simulation.core.settings import settings


engine = create_async_engine(settings.DB_DSN)


def generate_get_session(async_engine):
    async def _get_session():
        Session = _async_sessionmaker(
            bind=async_engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
            class_=AsyncSession,
        )
        session: AsyncSession = Session()
        try:
            yield session
        finally:
            await session.close()

    return _get_session


get_session = generate_get_session(engine)


async def drop_all(conn):
    await conn.run_sync(settings.BaseModel.metadata.drop_all)


async def create_all(conn):
    await conn.run_sync(settings.BaseModel.metadata.create_all)


async def __recreate_tables():
    print("Recritando tabelas")
    async with engine.begin() as conn:
        await drop_all(conn)
        await create_all(conn)
    print("Tabelas recriadas")


def recreate_tables():
    from asyncio import run

    run(__recreate_tables())
