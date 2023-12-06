from cars.economy import Economy
from decorators.v6 import V6
from decorators.vinyl import Vinyl
from decorators.leather import Leather


def main():
    car = Economy()
    show(car)

    car = V6(car)
    show(car)

    car = Vinyl(car)
    show(car)

    car = Leather(car)
    show(car)


def show(car):
    print(f"Description: {car.description}; Cost: {car.cost}")


if __name__ == '__main__':
    main()
