from abc import ABC, abstractmethod

class IProduct(ABC):
    @astractmethod
    get_price(self) -> int:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass