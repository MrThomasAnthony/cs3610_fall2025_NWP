from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def SAY_SOMETHING(self) -> str:
        pass