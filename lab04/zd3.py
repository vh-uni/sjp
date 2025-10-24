#!/usr/bin/python3

from typing import List


class Student:
    quantity = 0

    def __init__ (self):
        self.name = ""
        self.last_name = ""
        self.index = None
        self.marks = []

        Student.quantity += 1

    def give_name(self, name: str, last_name: str) -> None:
        self.name = name
        self.last_name = last_name

    def give_mark(self, mark: int) -> None:
        self.marks.append(mark)

    def get_marks(self) -> List[int]:
        return self.marks

    def give_index(self, index: int) -> None:
        self.index = index

    def say_hello(self) -> None:
        print(f"Hello! I'm {self.name} {self.last_name} and my index is {self.index}")

    def calculate_average(self) -> float:
        return sum(self.marks) / len(self.marks)


def main() -> None:
    s1 = Student()
    print(f"Students quantity: {s1.quantity}")
    s2 = Student()
    print(f"Students quantity: {s2.quantity}")
    s3 = Student()
    print(f"Students quantity: {s3.quantity}")

    print("\n")
    print(f"Students quantity: {s1.quantity}")
    print(f"Students quantity: {Student.quantity}")

if __name__ == "__main__":
    main()
