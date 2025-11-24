from FactoryMethodZoo.ProductInterface.IAnimal import IAnimal

class GrizzlyBear(IAnimal):
    def SAY_SOMETHING(self) -> str:
        return "Roaring loudly!"