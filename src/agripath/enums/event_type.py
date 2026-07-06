from enum import StrEnum


class EventType(StrEnum):
    HARVESTING = "harvesting"
    PACKAGING = "packaging"
    STORAGE = "storage"
    TRANSPORTATION = "transportation"

    @property
    def label(self) -> str:
        return self.value.replace("_", " ").title()
