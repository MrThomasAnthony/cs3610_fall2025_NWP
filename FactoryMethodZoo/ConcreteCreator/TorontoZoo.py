from typing import List

from ProductInterface.IAnimal import IAnimal
from ConcreteProducts.Lion import Lion
from ConcreteProducts.Elephant import Elephant
from ConcreteProducts.Penguin import Penguin
from ConcreteProducts.WhiteBear import WhiteBear

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
        return "Welcome to the Toronto Zoo! Our Itinerary: \n1) African Savanna. \n2) Tundra Trek"