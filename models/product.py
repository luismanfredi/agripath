from dataclasses import dataclass, field

from models.event import Event


@dataclass
class Product:
    id_: str
    name: str
    events: list[Event] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.events is None:
            self.events: list[Event] = []

    def __str__(self) -> str:
        return f"{self.name} - {self.id_}"

    def add_event(self, description: str, registered_by: str) -> None:
        self.events.append(Event(description, registered_by))

    def print_history(self) -> None:
        print(self)
        for item in self.events:
            print(item)
