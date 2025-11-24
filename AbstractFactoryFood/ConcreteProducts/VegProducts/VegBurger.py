from AbstractProducts.Burger import Burger

class VegBurger(Burger):
    def __init__(self, price = 9.99, calories = 750, description = "This is a tasty Burger"):
        self._price = price
        self._calories = calories
        self._description = description
        
    def get_price(self) -> int:
        return self._price

    def get_description(self) -> str:
        return self._description
    
    def showVegBurgerAdver() -> str:
        return "Try our delicious and healthy Veg Burger!"