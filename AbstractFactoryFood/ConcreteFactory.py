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
    def create_burger(self) -> VegBurger:
        return VegBurger()

    def create_pizza(self) -> VegPizza:
        return VegPizza()

    def create_noodles(self) -> VegNoodles:
        return VegNoodles()

    def create_cutlet(self) -> VegCutlet:
        return VegCutlet()

class NonVegetarianFactory(FoodFactory):
    def create_burger(self) -> NonVegBurger:
        return NonVegBurger()

    def create_pizza(self) -> NonVegPizza:
        return NonVegPizza()

    def create_noodles(self) -> NonVegNoodles:
        return NonVegNoodles()

    def create_cutlet(self) -> NonVegCutlet:
        return NonVegCutlet()