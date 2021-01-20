from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):

    api_key: SecretStr = "23c202de6cmsha4bcc9967b2583bp18c424jsn7a60a0d29687"
    host: str = "realtor.p.rapidapi.com"

    pollution_api_key: SecretStr = "2d638766-0d7d-43cf-9c8b-f644b4b32e68"

    openweathermap_api: SecretStr = "3e2dd42d919a54ac860fca0d16417fc3"


settings = Settings()
