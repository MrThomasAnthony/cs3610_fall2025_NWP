from AbstractProducts.Pizza import Pizza

class NonVegPizza(Pizza):
    def __init__(self, price = 15.70, calories = 900, descr = "This is a tasty Non-Veg Pizza", size = "Medium"):
        self._price = price
        self._calories = calories
        self._size = size
        self._descr = descr