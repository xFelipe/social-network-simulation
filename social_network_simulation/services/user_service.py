from social_network_simulation.models.user_model import UserModel
from social_network_simulation.services.base_service import BaseService
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List


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
