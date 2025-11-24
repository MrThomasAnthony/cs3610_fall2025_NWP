from FactoryMethodZoo.ProductInterface.IAnimal import IAnimal

class Moose(IAnimal):
    def SAY_SOMETHING(self) -> str:
        return "Bellowing!"