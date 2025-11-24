from typing import List

from ProductInterface.IAnimal import IAnimal
from ConcreteProducts.Penguin import Penguin
from ConcreteProducts.GrizzlyBear import GrizzlyBear
from ConcreteProducts.Moose import Moose

from CreatorInterface.IZoo import Zoo

class CalgaryZoo(Zoo):
    def create_Animals(self) -> List[IAnimal]:
        return [
            Penguin(),
            GrizzlyBear(),
            Moose()
        ]

    def get_itinerary(self) -> str:
        return "Welcome to the Calgary Zoo! Our Itinerary: \n1) Penguin Plunge. \n2) Wild Canada."