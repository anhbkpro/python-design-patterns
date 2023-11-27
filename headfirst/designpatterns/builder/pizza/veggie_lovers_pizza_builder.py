from pizza_builder import PizzaBuilder

class VeggieLoversPizzaBuilder(PizzaBuilder):
    def add_cheese(self):
        self._pizza.toppings.append('parmesan')

    def add_sauce(self):
        self._pizza.toppings.append('sauce')

    def add_tomatoes(self):
        self._pizza.toppings.append('chopped tomatoes')

    def add_garlic(self):
        self._pizza.toppings.append('garlic')

    def add_olives(self):
        self._pizza.toppings.append('olives')

    def add_spinach(self):
        self._pizza.toppings.append('spinach')

    def add_pepperoni(self):
        # never EVER add Pepperoni to veggie lovers pizza
        pass

    def add_sausage(self):
        # never EVER add sausage to veggie lovers pizza
        pass
