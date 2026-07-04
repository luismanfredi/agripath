import pytest

from enums.event_type import EventType
from models.product import Product


@pytest.fixture
def event_type() -> EventType:
    return EventType("harvesting")


@pytest.fixture
def product() -> Product:
    return Product("123_test", "TEST")


def test_product_init(product: Product) -> None:
    assert product.id_ == "123_test"
    assert product.name == "TEST"
    assert product.events == []


def test_product_str(product: Product) -> None:
    assert str(product) == f"{product.name} - {product.id_}"


def test_add_event_to_product(product: Product, event_type: EventType) -> None:
    product.add_event(event_type, "Test description", "TEST")

    assert product.events[0].event_type == event_type
    assert product.events[0].description == "Test description"
    assert product.events[0].registered_by == "TEST"
