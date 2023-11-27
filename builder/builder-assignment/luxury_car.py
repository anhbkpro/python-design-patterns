from abs_builder import AbsBuilder

class LuxuryCar(AbsBuilder):
  def add_vin_number(self):
    self._car.vin_number = 'Luxury Car Vin Number'

  def add_model(self):
    self._car.model = 'Luxury Car Model'

  def add_color(self):
    self._car.color = 'Luxury Car Color'

  def add_engine(self):
    self._car.engine = 'Luxury Car Engine'
