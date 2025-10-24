#!/usr/bin/python3


class StudentA:
    def __init__ (self, name: str, last_name: str):
        self.name = name
        self.last_name = last_name


class StudentB(StudentA):
    def __init__ (self, name: str, last_name: str):
        super().__init__(name, last_name)

    def __repr__(self) -> str:
        return f"{self.name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.name} {self.last_name}"


def main():
    s1 = StudentA("John", "Smith")
    s2 = StudentB("Joe", "Doe")
    print(f"StudentA - {s1}")
    print(f"StudentB - {s2}")

    print("\n")

    print(f"repr(StudentA) - {repr(s1)}")
    print(f"repr(StudentB) - {repr(s2)}")

if __name__ == "__main__":
    main()