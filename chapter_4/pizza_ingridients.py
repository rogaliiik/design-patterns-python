from abc import ABC, abstractmethod


class PizzaIngredientFactory(ABC):
    @abstractmethod
    def createDough(self):
        pass

    @abstractmethod
    def createSauce(self):
        pass

    @abstractmethod
    def createCheese(self):
        pass

    @abstractmethod
    def createVeggies(self):
        pass

    @abstractmethod
    def createPepperoni(self):
        pass

    @abstractmethod
    def createClam(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ThinCrustDough()

    def createSauce(self):
        return MarinaraSauce()

    def createCheese(self):
        return RaggianoCheese()

    def createVeggies(self):
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def createPepperoni(self):
        return SlicePepperoni()

    def createClam(self):
        return FreshClams()


class PizzaStore(ABC):
    def orderPizza(self, pizza_type):
        pizza = self.createPizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def createPizza(self, pizza_type):
        pass


class NYPizzaStore(PizzaStore):
    def createPizza(self, item):
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()

        if item == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("New York Style Cheese Pizza")
        # elif item == 'veggie':
        #     pizza = VeggiePizza(ingredient_factory)
        #     pizza.set_name("New York Style Veggie Pizza")
        # elif item == 'clam':
        #     pizza = ClamPizza(ingredient_factory)
        #     pizza.set_name("New York Style Clam Pizza")
        # elif item == 'pepperoni':
        #     pizza = PepperoniPizza(ingredient_factory)
        #     pizza.set_name("New York Style Pepperoni Pizza")
        return pizza


class Pizza(ABC):
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.veggies = None
        self.cheese = None
        self.pepperoni = None
        self.clam = None

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print('Bake for 25 minutes at 350')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def toString(self):
        """Код вывода описания пиццы"""
        pass


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        super().__init__()
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print('Preparing ' + self.name)
        dough = self.ingredient_factory.createDough()
        sauce = self.ingredient_factory.createSauce()
        cheese = self.ingredient_factory.createCheese()


class ThinCrustDough:
    pass


class MarinaraSauce:
    pass


class RaggianoCheese:
    pass


class Garlic:
    pass


class Onion:
    pass


class Mushroom:
    pass


class RedPepper:
    pass


class SlicePepperoni:
    pass


class FreshClams:
    pass


class PizzaTestDrive:
    def main(self):
        nyPizzaStore = NYPizzaStore()
        pizza = nyPizzaStore.orderPizza('cheese')
        print(f'Ethan ordered a {pizza.get_name()}')


PizzaTestDrive().main()
