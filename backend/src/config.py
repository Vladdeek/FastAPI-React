from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    CMC_API_KEY: str  # Аннотируйте как строку

    class Config:
        env_file = ".env"  # Укажите путь к файлу .env

settings = Settings()
