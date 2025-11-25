from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    service_name: str = "template-service"
    service_id: int = 0
    registry_url: str = "https://registry.example.com"
    jwt_secret: str = "your-secret-here"
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"

settings = Settings()

