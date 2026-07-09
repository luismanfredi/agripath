from agripath.db import db_models  # noqa: F401
from agripath.db.database import Base, engine


def init_db() -> None:
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()
    print("Tables created successfully!")
