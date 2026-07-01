from datetime import datetime

class Event:
    def __init__(self,  description: str, registered_by: str) -> None:
        self.description = description
        self.registered_by = registered_by
        self.registry_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    
    def __str__(self) -> str:
        return f'[{self.registry_time}] {self.description}, registered by "{self.registered_by}"'