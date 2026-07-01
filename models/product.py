from dataclasses import dataclass
from event import Event

@dataclass
class Product:
    id: str
    name: str
    events: list[Event] = None

    def __post_init__(self):
        if self.events is None:
            self.events = []

    def __str__(self) -> str:
        return f"{self.name} - {self.id}"
    
    def add_event(self, description: str, registered_by: str) -> None:
            self.events.append(Event(description, registered_by))

    def print_history(self) -> None:
        print(self)
        for item in self.events:
            print(item)