from .abs_car import AbsCar


class Sport(AbsCar):
    @property
    def description(self):
        return 'Sport Car'

    @property
    def cost(self):
        return 20000.00
