from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    huggingface_api_key: str = Field(env="HUGGINGFACE_API_KEY")


settings = Settings()
