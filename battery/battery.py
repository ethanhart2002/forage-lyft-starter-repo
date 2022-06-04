from abc import ABC
from car import Car


class Battery(ABC):
    def needs_service(self):
        pass
