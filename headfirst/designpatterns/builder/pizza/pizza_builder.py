import abc
from pizza import Pizza


class PizzaBuilder(abc.ABC):
    def get_pizza(self):
        return self._pizza

    def new_pizza(self, name):
        self._pizza = Pizza(name)

    @abc.abstractmethod
    def add_cheese(self):
        pass

    @abc.abstractmethod
    def add_sauce(self):
        pass

    @abc.abstractmethod
    def add_tomatoes(self):
        pass

    @abc.abstractmethod
    def add_garlic(self):
        pass

    @abc.abstractmethod
    def add_olives(self):
        pass

    @abc.abstractmethod
    def add_spinach(self):
        pass

    @abc.abstractmethod
    def add_pepperoni(self):
        pass

    @abc.abstractmethod
    def add_sausage(self):
        pass
