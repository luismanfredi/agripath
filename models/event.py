from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass(frozen=True)
class Event:
    description: str
    registered_by: str
    registry_time: datetime | None = None

    def __post_init__(self) -> None:
        if self.registry_time is None:
            object.__setattr__(self, "registry_time", datetime.now(UTC))

    def __str__(self) -> str:
        return (
            f"[{self.registry_time:%Y/%m/%d %H:%M:%S}] {self.description}, "
            f'registered by "{self.registered_by}"'
        )
