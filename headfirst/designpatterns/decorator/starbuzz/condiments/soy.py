from .condiment_decorator import CondimentDecorator


class Soy(CondimentDecorator):
    @property
    def description(self):
        return self.beverage.description + ', Soy'

    @property
    def cost(self):
        return self.beverage.cost + 0.15
