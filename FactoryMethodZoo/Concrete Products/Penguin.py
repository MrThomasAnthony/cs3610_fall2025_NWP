from FactoryMethodZoo.ProductInterface.IAnimal import IAnimal

class Penguin(IAnimal):
    def SAY_SOMETHING(self) -> str:
        return "Squawking!"