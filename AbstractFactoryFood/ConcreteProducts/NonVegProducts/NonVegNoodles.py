from AbstractProducts.Noodles import Noodles

class NonVegNoodles(Noodles):
    def __init__(self, price = 10.50, calories = 500, descr = "This is a tasty Non-Veg Noodle Bowl"):
        self._price = price
        self._calories = calories
        self._descr = descr