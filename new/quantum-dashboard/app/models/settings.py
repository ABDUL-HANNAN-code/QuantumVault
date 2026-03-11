from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime
from pydantic import BaseSettings
import ast

class Settings(BaseSettings):
    CORS_ORIGINS: list = []
    ALLOWED_HOSTS: list = []

    class Config:
        env_file = ".env"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Parse stringified lists from .env
        if isinstance(self.CORS_ORIGINS, str):
            self.CORS_ORIGINS = ast.literal_eval(self.CORS_ORIGINS)
        if isinstance(self.ALLOWED_HOSTS, str):
            self.ALLOWED_HOSTS = ast.literal_eval(self.ALLOWED_HOSTS)

settings = Settings()
class UserSetting(BaseModel):
    id: Optional[str] = None
    user_id: str
    setting_key: str
    setting_value: Any
    updated_at: datetime = datetime.utcnow()
