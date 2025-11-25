from AbstractFactoryInterface import FoodFactory
from ConcreteProducts.VegProducts.VegBurger import VegBurger
from ConcreteProducts.VegProducts.VegPizza import VegPizza
from ConcreteProducts.VegProducts.VegNoodles import VegNoodles
from ConcreteProducts.VegProducts.VegCutlet import VegCutlet
from ConcreteProducts.NonVegProducts.NonVegBurger import NonVegBurger
from ConcreteProducts.NonVegProducts.NonVegPizza import NonVegPizza
from ConcreteProducts.NonVegProducts.NonVegNoodles import NonVegNoodles
from ConcreteProducts.NonVegProducts.NonVegCutlet import NonVegCutlet

class VegetarianFactory(FoodFactory):
    def create_burger(self, price: float, calories: int, descr: str) -> VegBurger:
        return VegBurger(price, calories, descr)

    def create_pizza(self, price: float, calories: int, size: str, descr: str) -> VegPizza:
        return VegPizza(price, calories, descr, size)

    def create_noodles(self, price: float, calories: int, descr: str) -> VegNoodles:
        return VegNoodles(price, calories, descr)

    def create_cutlet(self, price: float, calories: int, descr: str) -> VegCutlet:
        return VegCutlet(price, calories, descr)

class NonVegetarianFactory(FoodFactory):
    def create_burger(self, price: float, calories: int, descr: str) -> NonVegBurger:
        return NonVegBurger(price, calories, descr)

    def create_pizza(self, price: float, calories: int, size: str, descr: str) -> NonVegPizza:
        return NonVegPizza(price, calories, descr, size)

    def create_noodles(self, price: float, calories: int, descr: str) -> NonVegNoodles:
        return NonVegNoodles(price, calories, descr)

    def create_cutlet(self, price: float, calories: int, descr: str) -> NonVegCutlet:
        return NonVegCutlet(price, calories, descr)