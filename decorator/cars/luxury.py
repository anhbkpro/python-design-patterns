from .abs_car import AbsCar


class Luxury(AbsCar):
    @property
    def description(self):
        return 'Luxury Car'

    @property
    def cost(self):
        return 40000.00
