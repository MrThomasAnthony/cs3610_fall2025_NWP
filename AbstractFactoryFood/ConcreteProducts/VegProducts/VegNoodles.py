from AbstractFactoryFood.Noodles import Noodles

class VegNoodles(Noodles):
    def __init__(self, price = 9.99, calories = 860, description = "This is a tasty Noodle Bowl"):
        self._price = price
        self._calories = calories
        self._description = description
        
    def get_price(self) -> int:
        return self._price

    def get_description(self) -> str:
        return self._description
    
    def showVegBoodlesAdver() -> str:
        return "Try our delicious and healthy Veg Noodles!"