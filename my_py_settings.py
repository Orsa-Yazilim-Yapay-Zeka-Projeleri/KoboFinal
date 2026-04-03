from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    HUGGING_FACE_API_KEY : str 
    MISTRAL_API_KEY : str 

    model_config = SettingsConfigDict(env_file=".env")


settings_variable = Settings()

