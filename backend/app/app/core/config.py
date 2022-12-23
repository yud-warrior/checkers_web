import os

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn


class Settings(BaseSettings):
    API_V1_STR: str = "api/v1"
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = \
        os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

    SQLALCHEMY_DATABASE_URI: PostgresDsn = os.environ.get("DATABASE_URL")

    class Config:
        case_sensitive = True


settings = Settings()
