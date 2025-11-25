from typing import List, Dict, Any
from ConcreteFactory import VegetarianFactory, NonVegetarianFactory
from IProduct import IProduct

AvailableFood: Dict[str, Any] = {
    "veg": VegetarianFactory(),
    "nonveg": NonVegetarianFactory()
}

def makeOrder(prodNames: List[str]) -> List[IProduct]:
    
    order: List[IProduct] = []
    for name in prodNames:
        parts = name.lower().split("_", 1)
        if len(parts) != 2:
            continue
        diet_key, item = parts
        factory = AvailableFood.get(diet_key)
        if factory is None:
            continue

        if item == "burger":
            order.append(factory.create_burger(9.99, 750, "Tasty Burger"))
        elif item == "pizza":
            order.append(factory.create_pizza(14.99, 900, "Medium", "Tasty Pizza"))
        elif item == "noodles":
            order.append(factory.create_noodles(10.50, 500, "Tasty Noodles"))
        elif item == "cutlet":
            order.append(factory.create_cutlet(12.99, 780, "Tasty Cutlet"))
    return order

def getOrderDescription(products: List[IProduct]) -> str:
    lines: List[str] = []
    for p in products:
        try:
            lines.append(f"${p.get_price():.2f} - {p.get_description()}")
        except Exception:
            lines.append(str(p))
    return "\n".join(lines)

def main() -> None:
    sample_names = [
        "veg_burger",
        "veg_pizza",
        "veg_noodles",
        "nonveg_burger",
        "nonveg_pizza",
        "nonveg_noodles",
        "nonveg_cutlet"
    ]

    order = makeOrder(sample_names)
    print("--- Order ---")
    print(getOrderDescription(order))

if __name__ == "__main__":
    main()