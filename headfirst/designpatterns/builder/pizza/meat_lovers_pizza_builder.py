from pizza_builder import PizzaBuilder


class MeatLoversPizzaBuilder(PizzaBuilder):
    def add_cheese(self):
        self._pizza.toppings.append('mozzarella')

    def add_sauce(self):
        self._pizza.toppings.append('tomato')

    def add_tomatoes(self):
        self._pizza.toppings.append('sliced tomatoes')

    def add_garlic(self):
        self._pizza.toppings.append('garlic')

    def add_olives(self):
        #  never add olives to meat lovers pizza
        pass

    def add_spinach(self):
        # never add spinach to meat lovers pizza
        pass

    def add_pepperoni(self):
        self._pizza.toppings.append('pepperoni')

    def add_sausage(self):
        self._pizza.toppings.append('sausage')
