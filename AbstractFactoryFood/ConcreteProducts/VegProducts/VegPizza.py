from AbstractProducts.Pizza import Pizza

class VegPizza(Pizza):
    def __init__(self, price = 16.99, calories = 1200, descr = "This is a tasty Pizza", size = "Medium"):
        self._price = price
        self._calories = calories
        self._size = size
        self._descr = descr
    
    def showVegPizzaAdver() -> str:
        return "Try our delicious Veg Pizza!"