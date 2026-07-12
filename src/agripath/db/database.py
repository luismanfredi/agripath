from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from agripath.config import DATABASE_URL

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL was not found in .env")

engine: Engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


SessionLocal = sessionmaker(bind=engine)
