from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from social_network_simulation.core.settings import settings
import logging
from social_network_simulation.core.deps import setup_logging


setup_logging()
logger = logging.getLogger(__name__)


engine = create_async_engine(settings.DB_DSN)


async def get_session():
    Session = async_sessionmaker(
        bind=engine,
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


async def drop_all(conn):
    logger.info("Deletando todas as tabelas")
    await conn.run_sync(settings.BaseModel.metadata.drop_all)


async def create_all(conn):
    logger.info("Criando todas as tabelas")
    await conn.run_sync(settings.BaseModel.metadata.create_all)


async def __recreate_tables():
    async with engine.begin() as conn:
        await drop_all(conn)
        await create_all(conn)
    logger.info("Tabelas recriadas")


def recreate_tables():
    from asyncio import run

    run(__recreate_tables())
