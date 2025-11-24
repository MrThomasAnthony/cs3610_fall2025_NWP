from abc import ABC, abstractmethod

class Noodles(ABC):
    @abstractmethod
    def get_price(self) -> int:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass