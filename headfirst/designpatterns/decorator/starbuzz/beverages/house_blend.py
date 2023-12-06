from .beverage import Beverage


class HouseBlend(Beverage):
    def __init__(self):
        self._description = "House Blend Coffee"

    @property
    def description(self):
        return self._description

    @property
    def cost(self):
        return .89
