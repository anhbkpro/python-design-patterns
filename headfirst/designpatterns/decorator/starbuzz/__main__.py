from beverages.espresso import Espresso
from condiments.mocha import Mocha
from condiments.soy import Soy


def main():
    beverage = Espresso()
    print(f'{beverage.description} ${beverage.cost}')
    beverage = Mocha(beverage)
    print(f'{beverage.description} ${beverage.cost}')
    beverage = Soy(beverage)
    print(f'{beverage.description} ${beverage.cost}')


if __name__ == '__main__':
    main()
