from ConcreteCreator import TorontoZoo, CalgaryZoo

def main():
    print("--- Visiting Toronto ---")
    toronto = TorontoZoo.TorontoZoo()
    toronto.startVisit()

    print("--- Visiting Calgary ---")
    calgary = CalgaryZoo.CalgaryZoo()
    calgary.startVisit()

if __name__ == "__main__":
    main()