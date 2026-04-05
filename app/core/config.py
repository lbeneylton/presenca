import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    ENV: str = os.getenv("ENV", "DEV")
    DATABASE_URL: str | None = os.getenv("DATABASE_URL")
    DB_TEST: str = os.getenv("DB_TEST", "test.db")
    DATABASE_URLENV: str = os.getenv("DATABASE_URLENV", "")

    @property
    def sqlalchemy_url(self) -> str:
        if self.ENV == "DEV":
            return self.DATABASE_URLENV

        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL não definida no .env")

        return self.DATABASE_URL


DB_settings = Settings()
print(f"\nDATABASE URL: {DB_settings.sqlalchemy_url}\n")
