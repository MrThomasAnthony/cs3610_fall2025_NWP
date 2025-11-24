from abc import ABC, abstractmethod
from AbstractProducts.Burger import Burger
from AbstractProducts.Pizza import Pizza
from AbstractProducts.Noodles import Noodles
from AbstractProducts.Cutlet import Cutlet

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