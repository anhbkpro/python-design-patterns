from .abs_decorator import AbsDecorator


class White(AbsDecorator):
    @property
    def description(self):
        return self.car.description + ', White'

    @property
    def cost(self):
        return self.car.cost + 800.00
