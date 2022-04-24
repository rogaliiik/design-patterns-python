from abc import ABC, abstractmethod


class Beverage(ABC):
    description = "Unknown beverage"

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass


class CondimentDecorator(Beverage, ABC):
    @abstractmethod
    def get_description(self):
        pass


class Espresso(Beverage):
    def __init__(self, description="Espresso"):
        self.description = description

    def cost(self):
        return 1.99


class HouseBlend(Beverage):
    def __init__(self, description="House Blend"):
        self.description = description

    def cost(self):
        return 0.89


class DarkRoast(Beverage):
    def __init__(self, description="Dark Roast"):
        self.description = description

    def cost(self):
        return 0.99


class Decaf(Beverage):
    def __init__(self, description="Decaf"):
        self.description = description

    def cost(self):
        return 1.05


class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return 0.20 + self.beverage.cost()


class Soy(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return 0.15 + self.beverage.cost()


class Whip(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def cost(self):
        return 0.10 + self.beverage.cost()


class StarbuzzCoffee:
    def main(self):
        beverage = Espresso()
        print(beverage.get_description() + " $ " + str(beverage.cost()))

        beverage2 = DarkRoast()
        beverage2 = Mocha(beverage2)
        beverage2 = Mocha(beverage2)
        beverage2 = Whip(beverage2)
        print(beverage2.get_description() + " $ " + str(beverage2.cost()))

        beverage3 = HouseBlend()
        beverage3 = Soy(beverage3)
        beverage3 = Mocha(beverage3)
        beverage3 = Whip(beverage3)
        print(beverage3.get_description() + " $ " + str(beverage3.cost()))


StarbuzzCoffee().main()
