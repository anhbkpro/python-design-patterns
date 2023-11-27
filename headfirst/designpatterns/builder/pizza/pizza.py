class Pizza:

  def __init__(self, name):
    self.name = name
    self.toppings = []

  def prepare(self):
    print(f'Preparing {self.name}')
    print('Tossing dough...')
    print('Adding sauce...')
    print('Adding toppings:')
    for topping in self.toppings:
      print(f'\t{topping}')

  def bake(self):
    print('Bake for 25 minutes at 350')

  def cut(self):
    print('Cutting the pizza into diagonal slices')

  def box(self):
    print('Place pizza in official PizzaStore box')

  def __str__(self):
    display = ''
    display += f'---- {self.name} ----\n'
    for topping in self.toppings:
      display += f'{topping}\n'
    return display
