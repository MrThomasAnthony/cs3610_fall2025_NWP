from IProduct import IProduct

class Pizza(IProduct):
    def __init__ (self):
        self._price = 0
        self._calories = 0
        self._descr = ""
        self._size = "small"
        
    def get_price(self) -> int:
        return self._price
    
    def get_description(self) -> str:
        return self._descr
    
    