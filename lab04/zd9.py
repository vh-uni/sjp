#!/usr/bin/python3


class StudentA:
    def __init__ (self, name: str, last_name: str):
        print("Initializing StudentA")
        self.name = name
        self.last_name = last_name


class StudentB(StudentA):
    def __init__ (self, name: str, last_name: str):
        print("Initializing StudentB")
        super().__init__(name, last_name)

    def __repr__(self) -> str:
        return f"{self.name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"


def main():
    s1 = StudentA("John", "Smith")
    s2 = StudentB("Joe", "Doe")

if __name__ == "__main__":
    main()