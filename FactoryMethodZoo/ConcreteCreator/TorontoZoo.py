from typing import List

from ProductInterface.IAnimal import IAnimal
from ConcreteProducts import Lion, Elephant, Penguin, WhiteBear

from CreatorInterface.IZoo import Zoo

class TorontoZoo(Zoo):
    def create_Animals(self) -> List[IAnimal]:
        return [
            Lion(),
            Elephant(),
            Penguin(),
            WhiteBear(),
        ]

    def get_itinerary(self) -> str:
        return "Welcome to the Toronto Zoo! Our Itinerary: 1) African Savanna. 2) Tundra Trek"