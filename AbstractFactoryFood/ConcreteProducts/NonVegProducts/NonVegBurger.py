from AbstractProducts.Burger import Burger

class NonVegBurger(Burger):
    def __init__(self, price = 8.99, calories = 650, descr = "This is a tasty Non-Veg Burger"):
        self._price = price
        self._calories = calories
        self._descr = descr