from abc import ABC, abstractmethod
from typing import List

from ProductInterface.IAnimal import IAnimal

class Zoo(ABC):
    def __init__(self):
        self.animals: List[IAnimal] = self.create_Animals()
        self.ourItinerary = self.get_itinerary()
        
    @abstractmethod
    def create_Animals(self) -> List[IAnimal]:
        pass
    
    @abstractmethod
    def get_itinerary(self) -> str:
        pass
    
    def askEachAnimalToSaySomething(self) -> str:
        results = []
        for animal in self.animals:
            results.append(animal.SAY_SOMETHING())
        return "\n".join(results)
    
    def startVisit(self) -> str:
        print("-" * 30)
        print(self.ourItinerary)
        print("\nListen to our animals:")
        print(self.askEachAnimalToSaySomething())
        print("-" * 30)
        print("\n")