from abc import ABC, abstractmethod

class Battery(ABC):
    """Basic representation of a battery."""

    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self) -> bool:
        """Returns a boolean value based on whether the object needs service or not."""
        