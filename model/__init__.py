from abc import ABC, abstractmethod
from engine.__init__ import Engine
from battery.__init__ import Battery

class CarFactory(ABC):
    """Factory that creates a combination of engine and battery"""

    def get_engine(self) -> Engine:
        """Returns a new engine instance."""

    def get_battery(self) -> Battery:
        """Returns a new battery instance."""
