from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
import os

class Settings(BaseSettings):
    app_env: str = os.getenv("APP_ENV", "dev")
    database_url: str = os.getenv("DATABASE_URL", "postgresql+psycopg://brain:brain@db:5432/brain")
    cors_origins: List[str] = [o.strip() for o in os.getenv("CORS_ORIGINS", "").split(",") if o.strip()]

    model_config = SettingsConfigDict(env_file=None)

settings = Settings()
