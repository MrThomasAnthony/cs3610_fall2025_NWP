from typing import List

from ProductInterface.IAnimal import IAnimal
from ConcreteProducts import Penguin, GrizzlyBear, Moose

from CreatorInterface.IZoo import Zoo

class CalgaryZoo(Zoo):
    def create_Animals(self) -> List[IAnimal]:
        return [
            Penguin(),
            GrizzlyBear(),
            Moose()
        ]

    def get_itinerary(self) -> str:
        return "Welcome to the Calgary Zoo! Our Itinerary: 1) Penguin Plunge. 2) Wild Canada."