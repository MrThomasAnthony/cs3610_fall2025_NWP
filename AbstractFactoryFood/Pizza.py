from AbstractFactoryFood.IProduct import IProduct

class Pizza(IProduct):
    def __init__(self, price: int, description: str):
        self._price = price
        self._calories = calories
        self._description = description
        self._size = size
        
    def get_price(self) -> int:
        return self._price

    def get_description(self) -> str:
        return self._description