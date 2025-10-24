#!/usr/bin/python3


class Student:
    student_index = 0

    def __init__ (self, name: str, last_name: str):
        self.name = name
        self.last_name = last_name
        self.index = Student.student_index

        Student.student_index += 1

    def __eq__(self, o: object) -> bool:
        """Compare students name and last name"""
        return self.name == o.name and self.last_name == o.last_name

    def __ne__(self, o: object) -> bool:
        """Compare students name and last name"""
        return self.name != o.name and self.last_name != o.last_name

    def __lt__(self, o: object) -> bool:
        """Compare student indexes"""
        return self.index < o.index

    def __gt__(self, o: object) -> bool:
        """Compare student indexes"""
        return self.index > o.index

    def __le__(self, o: object) -> bool:
        """Compare student indexes"""
        return self.index <= o.index

    def __ge__(self, o: object) -> bool:
        """Compare student indexes"""
        return self.index >= o.index


def main():
    s1 = Student("A", "B")
    s2 = Student("C", "D")

    print(f"{s1 == s2 = }")
    print(f"s1 != s2 = {s1 != s2}")
    print(f"{s1 > s2 = }")
    print(f"{s1 >= s2 = }")
    print(f"{s1 < s2 = }")
    print(f"{s1 <= s2 = }")

if __name__ == "__main__":
    main()