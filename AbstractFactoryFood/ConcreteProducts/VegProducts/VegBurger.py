from AbstractFactoryFood.Burger import Burger

class VegBurger(Burger):
    def __init__(self, price: int, calories: int, description: str):
        self._price = price
        self._calories = calories
        self._description = description
        
    def get_price(self) -> int:
        return self._price

    def get_description(self) -> str:
        return self._description
    
    def showVegBurgerAdver() -> str:
        return "Try our delicious and healthy Veg Burger!"