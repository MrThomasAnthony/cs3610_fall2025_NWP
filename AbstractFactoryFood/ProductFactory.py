from AbstractFactoryFood.Burger import Burger
from AbstractFactoryFood.Pizza import Pizza
from typing import List

class ProductFactory:
    def create_burger(self, burger_type: str, price: int, calories: int, description: str) -> Burger: