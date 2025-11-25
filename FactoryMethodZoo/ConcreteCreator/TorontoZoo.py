from typing import List

from ProductInterface.IAnimal import IAnimal
from ConcreteProducts.Lion import Lion
from ConcreteProducts.Elephant import Elephant
from ConcreteProducts.Penguin import Penguin
from ConcreteProducts.WhiteBear import WhiteBear

from CreatorInterface.IZoo import Zoo

animals={'lion': Lion, 'elephant': Elephant, 'penguin': Penguin, 'white_bear': WhiteBear}

class TorontoZoo(Zoo):
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
        return "Welcome to the Toronto Zoo! Our Itinerary: \n1) African Savanna. \n2) Tundra Trek"