from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"