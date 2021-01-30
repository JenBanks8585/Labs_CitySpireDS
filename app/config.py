from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):

    api_key: SecretStr 
    host: str
    pollution_api_key: SecretStr 
    openweathermap_api: SecretStr 
    walk_api: str
    
    class Config:
        env_file = ".env"


settings = Settings()
print(settings)
