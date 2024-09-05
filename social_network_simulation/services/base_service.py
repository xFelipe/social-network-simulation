from sqlalchemy import select, delete
from typing import List
from social_network_simulation.core.database import AsyncSession
from social_network_simulation.core.deps import setup_logging
import logging


setup_logging()
logger = logging.getLogger()


class BaseService:
    def __init__(self, Model):
        self.Model = Model

    async def get_all(self, session: AsyncSession):
        query = select(self.Model)
        result = await session.execute(query)
        items: List[self.Model] = result.scalars().all()
        return items

    async def create(self, entity, session: AsyncSession):
        session.add(entity)
        await session.commit()
        await session.refresh(entity)
        return entity

    async def get(self, id, session: AsyncSession):
        query = select(self.Model).where(self.Model.id == id)
        result = await session.execute(query)
        item = result.scalar_one_or_none()
        return item

    async def delete(self, id, session: AsyncSession):
        query = delete(self.Model).where(self.Model.id == id)
        await session.execute(query)
        await session.commit()
