from pizza_director import PizzaDirector

from meat_lovers_pizza_builder import MeatLoversPizzaBuilder
from veggie_lovers_pizza_builder import VeggieLoversPizzaBuilder

pizza_builder = PizzaDirector(MeatLoversPizzaBuilder())
pizza_builder.build_pizza("Meat Lovers")
pizza = pizza_builder.get_pizza()
print(pizza)

pizza_builder = PizzaDirector(VeggieLoversPizzaBuilder())
pizza_builder.build_pizza("Veggie Lovers")
pizza = pizza_builder.get_pizza()
print(pizza)
