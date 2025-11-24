from ProductInterface.IAnimal import IAnimal

class WhiteBear(IAnimal):
    def SAY_SOMETHING(self) -> str:
        return "Growling!"