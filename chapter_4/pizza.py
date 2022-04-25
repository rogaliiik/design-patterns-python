from abc import ABC, abstractmethod


# class SimplePizzaFactory:
#     def createPizza(self, pizza_type):
#         pizza = None
#         if pizza_type == 'cheese':
#             pizza = CheesePizza()
#         elif pizza_type == 'pepperoni':
#             pizza = PepperoniPizza()
#         elif pizza_type == 'clam':
#             pizza = ClamPizza()
#         elif pizza_type == 'veggie':
#             pizza = VeggiePizza()
#         return pizza


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


class NYStylePizzaStore(PizzaStore):
    def createPizza(self, pizza_type):
        if pizza_type == 'cheese':
            return NYStyleCheesePizza()
        # elif pizza_type == 'pepperoni':
        #     return  NYStylePepperoniPizza()
        # elif pizza_type == 'clam':
        #     return = NYStyleClamPizza()
        # elif pizza_type == 'veggie':
        #     return = NYStyleVeggiePizza()


class ChicagoStylePizzaStore(PizzaStore):
    def createPizza(self, pizza_type):
        if pizza_type == 'cheese':
            return ChicagoStyleCheesePizza()
        # elif pizza_type == 'pepperoni':
        #     return ChicagoStylePepperoniPizza()
        # elif pizza_type == 'clam':
        #     return ChicagoStyleClamPizza()
        # elif pizza_type == 'veggie':
        #     return ChicagoStyleVeggiePizza()


class Pizza:
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = None

    def prepare(self):
        print('Preparing ' + self.name)
        print('Tossing dough...')
        print('Adding sauce...')
        print('Adding toppings: ')
        for i in self.toppings:
            print(i)

    def bake(self):
        print('Bake for 25 minutes')

    def cut(self):
        print('Cutting the pizza into diagonal slices')

    def box(self):
        print('Place pizza in official PizzaStore box')

    def get_name(self):
        return self.name


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = ["Grated Reggiano Cheese"]


class ChicagoStyleCheesePizza(Pizza):
    def __init__(
            self,
            name='Chicago Style Deep Dish Cheese Pizza',
            dough='Extra Thick Crust Dough',
            sauce='Plum Tomato Cheese'
    ):
        super().__init__()
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = ['Shredded Mozarella Cheese']

        def cut(self):
            print("Cutting the pizza into square slices")


class PizzaTestDrive:
    def main(self):
        nyStore = NYStylePizzaStore()
        chicagoStore = ChicagoStylePizzaStore()
        pizza = nyStore.orderPizza('cheese')
        print(f'Ethan ordered a {pizza.get_name()}')
        pizza = chicagoStore.orderPizza("cheese")
        print(f'Joel ordered {pizza.get_name()} ')


PizzaTestDrive().main()
