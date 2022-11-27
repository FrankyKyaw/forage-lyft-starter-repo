from abc import ABC, abstractmethod

class Tire(ABC):
    """Basic representation of a tire."""

    @abstractmethod
    def needs_service(self) -> bool:
        """Returns a boolean value based on whether the object needs service or not."""
        