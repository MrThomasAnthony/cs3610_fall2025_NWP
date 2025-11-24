from ConcreteCreator import TorontoZoo, CalgaryZoo

def main():
    # Client Code
    print("--- Visiting Toronto ---")
    toronto = TorontoZoo()
    toronto.open_zoo()

    print("--- Visiting Calgary ---")
    calgary = CalgaryZoo()
    calgary.open_zoo()

if __name__ == "__main__":
    main()