from fastapi.routing import APIRouter
from fastapi import Depends
from social_network_simulation.services.user_service import UserService
from social_network_simulation.schemas.user_schema import UserSchema, UserPublic
from social_network_simulation.core.database import AsyncSession, get_session
from typing import List
from fastapi import status, HTTPException
from social_network_simulation.models.user_model import UserModel


router = APIRouter()

service = UserService()


@router.get("/", response_model=List[UserPublic])
async def list_users(session: AsyncSession = Depends(get_session)):
    return await service.get_all(session)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserPublic)
async def create_user(user: UserSchema, session: AsyncSession = Depends(get_session)):
    new_user = UserModel(
        name=user.name,
        username=user.username,
        password=user.password,
        birthday=user.birthday,
        sex=user.sex,
    )
    error = await service.validade_new_user(new_user, session)
    if error:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, error)
    new_user = await service.create(new_user, session)
    return new_user


@router.get("/{user_id}", response_model=UserPublic, status_code=status.HTTP_200_OK)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await service.get(user_id, session)
    if not user:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, f"Não existe usuário com id {user_id}."
        )
    return user
