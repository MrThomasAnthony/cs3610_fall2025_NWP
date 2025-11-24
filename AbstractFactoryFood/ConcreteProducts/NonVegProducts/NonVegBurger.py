from AbstractProducts.Burger import Burger

class NonVegBurger(Burger):
    def __init__(self, price = 8.99, calories = 650, description = "This is a tasty Non-Veg Burger"):
        self._price = price
        self._calories = calories
        self._description = description
        
    def get_price(self) -> int:
        return self._price

    def get_description(self) -> str:
        return self._description