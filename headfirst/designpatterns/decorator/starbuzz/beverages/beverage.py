from abc import ABC, abstractmethod


class Beverage(ABC):
    @property
    @abstractmethod
    def description(self):
        pass

    @property
    @abstractmethod
    def cost(self):
        pass
