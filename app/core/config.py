from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class DBConfig(BaseModel):
    db_url: str = os.environ["db_url"]


class Settings(BaseSettings):
    db: DBConfig = DBConfig()


settings = Settings()
