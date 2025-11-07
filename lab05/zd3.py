#!/usr/bin/python3

from random import seed, randint
from math import sqrt

seed()


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def calculate_triangle_area(a, b, c):
    semi_perimeter = (a + b + c) / 2
    area = sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
    return round(area, 2)


def main() -> None:
    a = randint(3, 10)
    b = randint(3, 10)
    c = randint(3, 10)

    print(f"Lengths are {a}, {b}, {c}.")
    print(f"Is it possible to build a triangle? {'Yes' if is_triangle(a, b, c) else 'No'}")

    if is_triangle(a, b, c):
        print(f"Area of the triangle is: {calculate_triangle_area(a, b, c)}")


if __name__ == "__main__":
    main()