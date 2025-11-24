from AbstractFactoryFood.AbstractProducts.Noodles import Noodles

class NonVegNoodles(Noodles):
    def __init__(self, price = 10.50, calories = 500, description = "This is a tasty Non-Veg Noodle Bowl"):
        self._price = price
        self._calories = calories
        self._description = description
        
    def get_price(self) -> int:
        return self._price

    def get_description(self) -> str:
        return self._description