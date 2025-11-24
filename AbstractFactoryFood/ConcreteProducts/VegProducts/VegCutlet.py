from AbstractProducts.Cutlet import Cutlet

class VegCutlet(Cutlet):
    def __init__(self, price = 14.99, calories = 800, description = "This is a tasty Cutlet"):
        self._price = price
        self._calories = calories
        self._description = description
        
    def get_price(self) -> int:
        return self._price

    def get_description(self) -> str:
        return self._description
    
    def showVegCutletAdver() -> str:
        return "Try our delicious and healthy Veg Cutlet!"