from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2] # backend/

ENV_FILE = BASE_DIR / ".env"

class Settings(BaseSettings):
    app_name: str = "CloudNotes API"
    env: str = "dev"
    
    database_url: str
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    
    redis_url: str
    
    aws_region: str
    s3_bucket: str
    
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        case_sensitive=False,
    )
        
settings = Settings()