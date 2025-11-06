#!/usr/bin/python3

from typing import List


class Student:
    def __init__ (self):
        self.name = ""
        self.last_name = ""
        self.index = None
        self.marks = []

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
        if len(self.marks) == 0:
            raise ZeroDivisionError("No marks available to calculate average.")
        return sum(self.marks) / len(self.marks)


def main() -> None:
    s = Student()
    s.give_name("Jane", "Doe")
    s.give_mark(5)  # wywołanie sposób 1
    Student.give_mark(s, 3)  # wywołanie sposób 2
    print(s.get_marks())

    s.give_index(0)
    s.say_hello()

    print(f"Student's average is {s.calculate_average()}")

if __name__ == "__main__":
    main()
