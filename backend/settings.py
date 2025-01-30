from pydantic_settings import BaseSettings
from pydantic import Field

from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    huggingface_api_key: str = Field(env="HUGGINGFACE_API_KEY")

settings = Settings()