from .condiment_decorator import CondimentDecorator


class SteamedMilk(CondimentDecorator):
    @property
    def description(self):
        return self.beverage.description + ', Steamed Milk'

    @property
    def cost(self):
        return self.beverage.cost + 0.10
