from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):

    api_key: SecretStr 
    host: str
    walk_api: str
    
    class Config:
        env_file = ".env"


settings = Settings()
print(settings)
