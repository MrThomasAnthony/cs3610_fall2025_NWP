from FactoryMethodZoo.ProductInterface.IAnimal import IAnimal

class Elephant(IAnimal):
    def SAY_SOMETHING(self) -> str:
        return "Trumpeting!"