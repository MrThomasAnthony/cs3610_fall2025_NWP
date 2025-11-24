from abc import ABC, abstractmethod

class Burger(ABC):
    @abstractmethod
    def get_price(self) -> int:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass