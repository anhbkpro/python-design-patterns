from abs_builder import AbsBuilder


class EconomyCar(AbsBuilder):
  def add_vin_number(self):
    self._car.vin_number = 'Economy Car Vin Number'

  def add_model(self):
    self._car.model = 'Economy Car Model'

  def add_color(self):
    self._car.color = 'Economy Car Color'

  def add_engine(self):
    self._car.engine = 'Economy Car Engine'
