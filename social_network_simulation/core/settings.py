from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.orm import declarative_base
from typing import Any


class Settings(BaseSettings):
    API_PORT: int
    API_HOST: str
    DB_DSN: str
    BaseModel: Any = declarative_base()
    API_V1_PREFIX: str = "/api/v1"

    model_config = SettingsConfigDict(
        extra="ignore", env_file=".env", env_file_encoding="utf-8"
    )


settings = Settings()
