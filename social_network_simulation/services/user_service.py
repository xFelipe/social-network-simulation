from social_network_simulation.models.user_model import UserModel
from social_network_simulation.services.base_service import BaseService
from social_network_simulation.schemas.user_schema import UserUpdateSchema
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional


class UserService(BaseService):
    def __init__(self):
        super().__init__(UserModel)

    async def validade_new_user(
        self, user: UserModel, session: AsyncSession
    ) -> List[str]:
        erros = []
        query = select(UserModel).where(UserModel.username == user.username)
        result = await session.execute(query)
        user_with_same_username = result.scalars().all()
        if user_with_same_username:
            erros.append(
                f"Já existe um usuário com username '{user.username}' cadastrado"
            )
        return erros

    async def update(
        self, user_id, user_new_data: UserUpdateSchema, session: AsyncSession
    ):
        user: Optional[UserModel] = await self.get(user_id, session)
        if not user:
            return

        if user_new_data.name:
            user.name = user_new_data.name
        if user_new_data.username:
            user.username = user_new_data.username
        if user_new_data.birthday:
            user.birthday = user_new_data.birthday
        if user_new_data.sex:
            user.sex = user_new_data.sex

        session.add(user)
        await session.commit()
        await session.refresh(user)

        return user
