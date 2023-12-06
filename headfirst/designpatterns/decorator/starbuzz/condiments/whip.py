from .condiment_decorator import CondimentDecorator


class Whip(CondimentDecorator):
    @property
    def description(self):
        return self.beverage.description + ', Whip'

    @property
    def cost(self):
        return self.beverage.cost + 0.10
