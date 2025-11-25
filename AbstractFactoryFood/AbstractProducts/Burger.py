from IProduct import IProduct

class Burger(IProduct):
    def __init__(self):
        self._price: float = 0.0
        self._calories: int = 0
        self._descr: str = ""

    def get_price(self) -> float:
        return self._price

    def get_description(self) -> str:
        return self._descr