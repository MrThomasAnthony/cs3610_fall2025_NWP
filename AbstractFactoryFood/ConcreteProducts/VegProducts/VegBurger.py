from AbstractProducts.Burger import Burger

class VegBurger(Burger):
    def __init__(self, price = 9.99, calories = 750, descr = "This is a tasty Burger"):
        self._price = price
        self._calories = calories
        self._descr = descr
    
    def showVegBurgerAdver() -> str:
        return "Try our delicious and healthy Veg Burger!"