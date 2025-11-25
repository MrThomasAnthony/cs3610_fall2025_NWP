from abc import ABC, abstractmethod

class FoodFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_burger(food) -> None:
        pass

    @staticmethod
    @abstractmethod
    def create_pizza(food) -> None:
        pass

    @staticmethod
    @abstractmethod
    def create_noodles(food) -> None:
        pass

    @staticmethod
    @abstractmethod
    def create_cutlet(food) -> None:
        pass