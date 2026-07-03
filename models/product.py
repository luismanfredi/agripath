from dataclasses import dataclass, field

from enums.event_type import EventType
from models.event import Event


@dataclass
class Product:
    id_: str
    name: str
    events: list[Event] = field(default_factory=list)

    def __str__(self) -> str:
        return f"{self.name} - {self.id_}"

    def add_event(
        self, event_type: EventType, description: str, registered_by: str
    ) -> None:
        self.events.append(Event(event_type, description, registered_by))
