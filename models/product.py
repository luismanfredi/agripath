from event import Event

class Product:
    def __init__(self, id: str, name: str) -> None:
        self.id = id
        self.name = name
        self.events = []

    def add_event(self, description: str, registered_by: str) -> None:
        self.events.append(Event(description, registered_by))

    def __str__(self) -> str:
        return f"{self.name} - {self.id}"
    
    def print_history(self) -> None:
        print(self)
        for item in self.events:
            print(item)