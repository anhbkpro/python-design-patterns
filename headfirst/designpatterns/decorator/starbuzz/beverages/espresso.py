from .beverage import Beverage


class Espresso(Beverage):
    def __init__(self):
        self._description = "Espresso"

    @property
    def description(self):
        return self._description

    @property
    def cost(self):
        return 1.99
