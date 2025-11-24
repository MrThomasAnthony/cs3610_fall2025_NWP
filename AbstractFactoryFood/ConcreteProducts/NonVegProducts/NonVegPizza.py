from AbstractFactoryFood.AbstractProducts.Pizza import Pizza

class NonVegPizza(Pizza):
    def __init__(self, price: int, calories: int, size: str, description: str):
        self._price = price
        self._calories = calories
        self._size = size
        self._description = description
        
    def get_price(self) -> int:
        return self._price

    def get_description(self) -> str:
        return self._description