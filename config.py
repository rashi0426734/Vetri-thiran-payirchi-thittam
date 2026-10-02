import os
from functools import lru_cache
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):
    app_name: str = os.getenv("APP_NAME", "EduGenie")
    app_version: str = os.getenv("APP_VERSION", "1.0.0")
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()
