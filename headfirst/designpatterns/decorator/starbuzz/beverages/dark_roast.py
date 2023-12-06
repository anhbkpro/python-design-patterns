from .beverage import Beverage


class DarkRoast(Beverage):
    def __init__(self):
        self._description = "Dark Roast Coffee"

    @property
    def description(self):
        return self._description

    @property
    def cost(self):
        return .99
