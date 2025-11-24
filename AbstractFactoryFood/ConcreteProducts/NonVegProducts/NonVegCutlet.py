from AbstractProducts.Cutlet import Cutlet

class NonVegCutlet(Cutlet):
    def __init__(self, price = 12.99, calories = 780, description = "This is a tasty Non-Veg Cutlet"):
        self._price = price
        self._calories = calories
        self._description = description
        
    def get_price(self) -> int:
        return self._price

    def get_description(self) -> str:
        return self._description