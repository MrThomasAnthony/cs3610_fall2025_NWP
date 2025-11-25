from AbstractProducts.Cutlet import Cutlet

class VegCutlet(Cutlet):
    def __init__(self, price = 14.99, calories = 800, descr = "This is a tasty Cutlet"):
        self._price = price
        self._calories = calories
        self._descr = descr
    
    def showVegCutletAdver() -> str:
        return "Try our delicious and healthy Veg Cutlet!"