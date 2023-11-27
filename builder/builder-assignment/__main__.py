from director import Director

from economy_car import EconomyCar
from luxury_car import LuxuryCar

car_builder = Director(EconomyCar())
car_builder.build_car()
car = car_builder.get_car()
car.list_characters()

car_builder = Director(LuxuryCar())
car_builder.build_car()
car = car_builder.get_car()
car.list_characters()
