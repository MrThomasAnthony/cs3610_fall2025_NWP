from abc import ABC, abstractmethod
from AbstractFactoryFood.AbstractProducts.Burger import Burger
from AbstractFactoryFood.AbstractProducts.Pizza import Pizza
from AbstractFactoryFood.AbstractProducts.Noodles import Noodles
from AbstractFactoryFood.AbstractProducts.Cutlet import Cutlet

class FoodFactory(ABC):
    @abstractmethod
    def create_burger(self) -> Burger:
        pass

    @abstractmethod
    def create_pizza(self) -> Pizza:
        pass

    @abstractmethod
    def create_noodles(self) -> Noodles:
        pass

    @abstractmethod
    def create_cutlet(self) -> Cutlet:
        pass