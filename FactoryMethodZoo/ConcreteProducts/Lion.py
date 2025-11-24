from FactoryMethodZoo.ProductInterface.IAnimal import IAnimal

class Lion(IAnimal):
    def SAY_SOMETHING(self) -> str:
        return "Roaring!"