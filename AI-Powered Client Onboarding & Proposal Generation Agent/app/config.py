import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    MAKE_WEBHOOK_URL: str = os.getenv("MAKE_WEBHOOK_URL", "")

settings = Settings()
