from AbstractFactoryFood.AbstractProducts.Pizza import Pizza

class NonVegPizza(Pizza):
    def __init__(self, price = 15.70, calories = 900, description = "This is a tasty Non-Veg Pizza", size = "Medium"):
        self._price = price
        self._calories = calories
        self._size = size
        self._description = description
        
    def get_price(self) -> int:
        return self._price

    def get_description(self) -> str:
        return self._description