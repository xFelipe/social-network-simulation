from enum import StrEnum
from social_network_simulation.core.settings import settings
from sqlalchemy import Column, Enum, String, Date, Integer
from social_network_simulation.models.utils import TimestampMixin


class Sex(StrEnum):
    male = "masculino"
    female = "feminino"
    another = "outro"


class UserModel(TimestampMixin, settings.BaseModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=200))
    username = Column(String(length=30))
    password = Column(String(length=80))
    birthday = Column(Date)
    sex = Column(Enum(Sex))
