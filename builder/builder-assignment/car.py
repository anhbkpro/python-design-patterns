class Car():
  def list_characters(self) -> None:
    print(f'\t{"Features":>15}:')
    print(f'\t{"VIN number":>15}: {self.vin_number}')
    print(f'\t{"Model":>15}: {self.model}')
    print(f'\t{"Color":>15}: {self.color}')
    print(f'\t{"Engine":>15}: {self.engine}')
