from AbstractFactoryFood.AbstractFactoryInterface import FoodFactory
from AbstractFactoryFood.AbstractProducts.Burger import Burger
from AbstractFactoryFood.AbstractProducts.Pizza import Pizza
from AbstractFactoryFood.AbstractProducts.Noodles import Noodles
from AbstractFactoryFood.AbstractProducts.Cutlet import Cutlet

class VegetarianFactory(FoodFactory):
    def create_burger(self) -> Burger:
        return VegBurger(9.99, 350, "A delicious vegetarian burger made with fresh vegetables and a tangy sauce.")

    def create_pizza(self) -> Pizza:
        return VegPizza(12.99, 500, "Medium", "A delightful vegetarian pizza topped with fresh veggies and mozzarella cheese.")

    def create_noodles(self) -> Noodles:
        return VegNoodles(10.99, 400, "A tasty bowl of vegetarian noodles cooked with fresh vegetables and flavorful spices.")

    def create_cutlet(self) -> Cutlet:
        return VegCutlet(14.99, 450, "A crispy and savory vegetarian cutlet made with a blend of vegetables and spices.")

class NonVegetarianFactory(FoodFactory):
    def create_burger(self) -> Burger:
        return NonVegBurger(13.99, 600, "A mouth-watering non-vegetarian burger made with juicy chicken patty and special sauce.")

    def create_pizza(self) -> Pizza:
        return NonVegPizza(15.99, 700, "Large", "A scrumptious non-vegetarian pizza loaded with chicken, pepperoni, and cheese.")

    def create_noodles(self) -> Noodles:
        return NonVegNoodles(12.99, 550, "A flavorful bowl of non-vegetarian noodles cooked with chicken and aromatic spices.")

    def create_cutlet(self) -> Cutlet:
        return NonVegCutlet(17.99, 650, "A delicious non-vegetarian cutlet made with minced chicken and a blend of spices.")