from abc import ABC, abstractmethod

class Battery(ABC):
    """Basic representation of a battery."""

    @abstractmethod
    def needs_service(self) -> bool:
        """Returns a boolean value based on whether the object needs service or not."""
        