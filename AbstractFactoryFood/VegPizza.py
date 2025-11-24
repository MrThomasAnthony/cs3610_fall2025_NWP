from AbstractFactoryFood.Pizza import Pizza

class VegPizza(Pizza):
    def __init__(self, price: int, calories: int, size: str, description: str):
        self._price = price
        self._calories = calories
        self._size = size
        self._description = description
        
    def get_price(self) -> int:
        return self._price

    def get_description(self) -> str:
        return self._description
    
    def showVegPizzaAdver() -> str:
        return "Try our delicious Veg Pizza, loaded with fresh vegetables and a blend of spices!"