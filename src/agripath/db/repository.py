from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from agripath.db.database import SessionLocal
from agripath.db.db_models import EventORM, ProductORM
from agripath.db.mappers import (
    event_to_orm,
    product_from_orm,
    product_to_orm,
)
from agripath.models.event import Event
from agripath.models.product import Product


def save_product(product: Product) -> None:
    orm: ProductORM = product_to_orm(product)
    with SessionLocal() as session:
        session.add(orm)
        try:
            session.commit()
        except IntegrityError as e:
            session.rollback()
            raise ValueError(f"Product with id '{product.id_}' already exists'") from e


def get_product(product_id: str) -> Product | None:
    with SessionLocal() as session:
        orm: ProductORM | None = session.get(ProductORM, product_id)
        if orm is None:
            return None
        return product_from_orm(orm)


def get_all_products() -> list[Product]:
    with SessionLocal() as session:
        orms: Sequence[ProductORM] = session.scalars(select(ProductORM)).all()
        return [product_from_orm(orm) for orm in orms]


def add_event_to_product(product_id: str, event: Event) -> None:
    with SessionLocal() as session:
        if session.get(ProductORM, product_id) is None:
            raise ValueError(f"Product {product_id} not found")

        event_orm: EventORM = event_to_orm(event, product_id)
        session.add(event_orm)
        session.commit()
