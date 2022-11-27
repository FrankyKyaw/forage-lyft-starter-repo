from abc import ABC, abstractmethod

class Engine(ABC):
    """Basic representation of an engine"""

    @abstractmethod
    def needs_service(self) -> bool:
        """Returns a boolean value based on whether the object needs service or not."""
