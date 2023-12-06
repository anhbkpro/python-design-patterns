from .condiment_decorator import CondimentDecorator


class Mocha(CondimentDecorator):
    @property
    def description(self):
        return self.beverage.description + ', Mocha'

    @property
    def cost(self):
        return self.beverage.cost + 0.20
