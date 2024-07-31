from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    GOOGLE_SEARCH_ENGINE_API_KEY: str
    GOOGLE_SEARCH_ENGINE_CX: str
    MAX_RESULTS: int = 5
    MAX_FILE_SIZE: int = 20
    DOWNLOAD_FOLDER: str = "downloaded_images"

    SEARCH_ENGINE_URI: str = "https://www.googleapis.com/customsearch/v1"

    class Config:
        env_file = '.env'


settings = Settings()
