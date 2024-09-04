from pydantic import BaseModel
from typing import Optional
from datetime import date
from social_network_simulation.models.user_model import Sex
from pydantic import Field


class UserSchema(BaseModel):
    name: str = Field(min_length=3, max_length=190)
    username: str = Field(min_length=3, max_length=190)
    password: str = Field(min_length=8, max_length=50)
    birthday: date
    sex: Sex


class UserPublic(UserSchema):
    id: Optional[int]

    # religions: List[str] = []
    # interest_and_hobbies: List[str] = []
    # values_and_beliefs: List[str] = []
    # social_status: List[str] = []
    # professional: List[str] = []
    # psychological: List[str] = []
    # education: List[str] = []
    # socioeconomic_situation: List[str] = []
