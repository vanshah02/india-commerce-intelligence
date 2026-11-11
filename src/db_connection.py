
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

PROJECT_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(PROJECT_ROOT / ".env")


def get_engine():
    connection_url = URL.create(
        drivername="postgresql+psycopg",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "5432")),
        database=os.getenv("DB_NAME"),
    )

    return create_engine(connection_url, pool_pre_ping=True)


if __name__ == "__main__":
    engine = get_engine()

    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database(), current_user, version()")
        )
        database, user, version = result.fetchone()

        print("Database connection successful!")
        print(f"Database: {database}")
        print(f"User: {user}")
        print(f"PostgreSQL: {version.split(',')[0]}")
