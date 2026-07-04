from dataclasses import FrozenInstanceError

import pytest

from enums.event_type import EventType
from models.event import Event


@pytest.fixture
def event_type() -> EventType:
    return EventType("harvesting")


@pytest.fixture
def event(event_type: EventType) -> Event:
    return Event(event_type, "Test description", "TEST")


def test_event_init(event: Event, event_type: EventType) -> None:
    assert event.event_type == event_type
    assert event.description == "Test description"
    assert event.registered_by == "TEST"
    assert event.registry_time is not None


def test_event_str(event: Event) -> None:
    event_str: str = (
        f"[{event.registry_time:%Y/%m/%d %H:%M:%S}] {event.description}, "
        f'registered by "{event.registered_by}"'
    )

    assert str(event) == event_str


def test_event_frozen(event: Event) -> None:
    with pytest.raises(FrozenInstanceError):
        setattr(event, "description", "x")
