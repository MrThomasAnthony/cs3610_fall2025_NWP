from AbstractProducts.Noodles import Noodles

class VegNoodles(Noodles):
    def __init__(self, price = 9.99, calories = 860, descr = "This is a tasty Noodle Bowl"):
        self._price = price
        self._calories = calories
        self._descr = descr
    
    def showVegNoodlesAdver() -> str:
        return "Try our delicious and healthy Veg Noodles!"