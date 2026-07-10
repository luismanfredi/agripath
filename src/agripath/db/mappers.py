from agripath.db.db_models import EventORM, ProductORM
from agripath.enums.event_type import EventType
from agripath.models.event import Event
from agripath.models.product import Product


def product_to_orm(product: Product) -> ProductORM:
    return ProductORM(
        id=product.id_,
        name=product.name,
        events=[event_to_orm(e, product.id_) for e in product.events],
    )


def product_from_orm(orm: ProductORM) -> Product:
    return Product(
        id_=orm.id, name=orm.name, events=[event_from_orm(e) for e in orm.events]
    )


def event_to_orm(event: Event, product_id: str) -> EventORM:
    return EventORM(
        event_type=event.event_type.value,
        description=event.description,
        registered_by=event.registered_by,
        registry_time=event.registry_time,
        product_id=product_id,
    )


def event_from_orm(orm: EventORM) -> Event:
    return Event(
        event_type=EventType(orm.event_type),
        description=orm.description,
        registered_by=orm.registered_by,
        registry_time=orm.registry_time,
    )
