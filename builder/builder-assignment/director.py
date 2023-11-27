from car import Car
from economy_car import EconomyCar
from luxury_car import LuxuryCar

class Director(object):
  def __init__(self, builder):
    self._builder = builder

  def build_car(self):
    self._builder.new_car()
    self._builder.add_vin_number()
    self._builder.add_model()
    self._builder.add_color()
    self._builder.add_engine()

  def get_car(self):
    return self._builder.get_car()
