from abc import ABC, abstractmethod

class IProduct(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass