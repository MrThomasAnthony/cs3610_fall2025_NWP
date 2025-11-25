from IProduct import IProduct

class Cutlet(IProduct):
    def __init__ (self):
        self._price = 0
        self._calories = 0
        self._descr = ""
        
    def get_price(self) -> int:
        return self._price
    
    def get_description(self) -> str:
        return self._descr