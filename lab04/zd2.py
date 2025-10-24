#!/usr/bin/python3


class Vehicle:
    def __init__(self, owner: str):
        self.owner = owner

    def get_sound(self) -> None:
        print("vehicle's brum brum")

    def get_owner(self) -> str:
        return self.owner


class Car(Vehicle):
    def __init__(self, owner: str, table: str):
        super().__init__(owner)
        self.table = table

    def get_sound(self) -> None:
        print("car's brum brum")

    def get_owner(self) -> str:
        return self.owner


def main() -> None:
    v = Vehicle(owner="Vehicle owner")
    c = Car(owner="Car owner", table="FG1242S")

    v.get_sound()
    c.get_sound()

    print("\n")

    # v.get_owner() powodowalo blad AttributeError dlatego, ze klasa Vehicle nie miala takiej metody
    # Zeby to poprawic, dodalem ta metode to klasy Vehicle.

    print(v.get_owner())
    print(c.get_owner())

if __name__ == "__main__":
    main()
