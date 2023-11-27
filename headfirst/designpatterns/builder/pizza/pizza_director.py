class PizzaDirector(object):
    def __init__(self, builder=None):
        self._builder = builder

    def build_pizza(self, name):
        self._builder.new_pizza(name)
        self._builder.add_cheese()
        self._builder.add_sauce()
        self._builder.add_tomatoes()
        self._builder.add_garlic()
        self._builder.add_olives()
        self._builder.add_spinach()
        self._builder.add_pepperoni()
        self._builder.add_sausage()

    def get_pizza(self):
        return self._builder.get_pizza()
