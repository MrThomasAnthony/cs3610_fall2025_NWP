from typing import Type
from ConcreteFactory import VegetarianFactory, NonVegetarianFactory

dict = {"Vegetarian": "VegetarianFactory()", "nonVegetarian": "NonVegetarianFactory()"}
AvailableFood = []

def veg_client_code(factory: Type[VegetarianFactory]) -> None:
    AvailableFood.append(factory.create_burger())
    AvailableFood.append(factory.create_pizza())
    AvailableFood.append(factory.create_noodles())
    AvailableFood.append(factory.create_cutlet())
    
def non_veg_client_code(factory: Type[NonVegetarianFactory]) -> None:
    AvailableFood.append(factory.create_burger())
    AvailableFood.append(factory.create_pizza())
    AvailableFood.append(factory.create_noodles())
    AvailableFood.append(factory.create_cutlet())

def main():
    veg_client_code(VegetarianFactory())
    non_veg_client_code(NonVegetarianFactory())
    
    for food in AvailableFood:
        print("1) Price: " + str(food.get_price()) + ", Description: " + food.get_description())
    
if __name__ == "__main__":
    main()