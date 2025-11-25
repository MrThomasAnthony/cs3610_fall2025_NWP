from typing import List, Type

from ProductInterface.IAnimal import IAnimal
from ConcreteProducts.Penguin import Penguin
from ConcreteProducts.GrizzlyBear import GrizzlyBear
from ConcreteProducts.Moose import Moose

from CreatorInterface.IZoo import Zoo

animals={'penguin': Penguin, 'grizzly_bear': GrizzlyBear, 'moose': Moose}

class CalgaryZoo(Zoo):
    def create_Animals(self) -> List[IAnimal]:
        # Instantiate all animals available in this concrete creator's registry
        created = []
        for animal_cls in animals.values():
            try:
                created.append(animal_cls())
            except Exception as _e:
                print(f"Failed to create animal: {_e}")
        return created

    def get_itinerary(self) -> str:
        return "Welcome to the Calgary Zoo! Our Itinerary: \n1) Penguin Plunge. \n2) Wild Canada."