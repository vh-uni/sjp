#!/usr/bin/python3

# Imports
from math import sqrt


def solve_quadratic_equation(a: float, b: float, c: float) -> tuple[float, float]:
    """
    Solve a quadratic equation: ax² + bx + c = 0.

    We assume, that equation always have two roots.
    :param a: float
    :param b: float
    :param c: float
    :return tuple: Roots of the equation.
    """
    delta = b ** 2 - 4 * a * c
    x1 = (-b - sqrt(delta)) / (2 * a)
    x2 = (-b + sqrt(delta)) / (2 * a)

    return x1, x2


def main() -> None:
    a = float(input("A = "))
    b = float(input("B = "))
    c = float(input("C = "))
    x1, x2 = solve_quadratic_equation(a, b, c)
    print(f"x1 = {x1}, x2 = {x2}")


if __name__ == '__main__':
    main()