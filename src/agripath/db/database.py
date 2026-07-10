import os

from dotenv import load_dotenv
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()

DATABASE_URL: str | None = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL was not found in .env")

engine: Engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


SessionLocal = sessionmaker(bind=engine)
