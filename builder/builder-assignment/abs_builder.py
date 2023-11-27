import abc
from car import Car

class AbsBuilder(abc.ABC):
  def get_car(self):
    return self._car

  def new_car(self):
    self._car = Car()

  @abc.abstractmethod
  def add_vin_number(self):
    pass

  @abc.abstractmethod
  def add_model(self):
    pass

  @abc.abstractmethod
  def add_color(self):
    pass

  @abc.abstractmethod
  def add_engine(self):
    pass
