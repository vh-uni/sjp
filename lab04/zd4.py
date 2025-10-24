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
        if not self._is_empty_names():
            print(f"Hello! I'm {self.name} {self.last_name} and my index is {self.index}")
        else:
            print("Name and last name mustn't be empty.")

    def calculate_average(self) -> float:
        return sum(self.marks) / len(self.marks)

    def _is_empty_names(self) -> bool:
        return self.name == "" or self.last_name == ""


def main() -> None:
    s = Student()
    s.say_hello()

    print(s._is_empty_names())

if __name__ == "__main__":
    main()
