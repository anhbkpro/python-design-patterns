from beverages.beverage import Beverage


class CondimentDecorator(Beverage):
    def __init__(self, beverage):
        self._beverage = beverage

    @property
    def beverage(self):
        return self._beverage
