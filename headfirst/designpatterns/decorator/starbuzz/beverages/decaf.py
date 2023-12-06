from .beverage import Beverage


class Decaf(Beverage):
    def __init__(self):
        self._description = "Decaf Coffee"

    @property
    def description(self):
        return self._description

    @property
    def cost(self):
        return 1.05
