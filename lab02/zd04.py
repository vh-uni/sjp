#!/usr/bin/python3

# Imports
from math import pi


def calc_circle_params(radius: float) -> tuple[float, float]:
    """
    Calculate the area of a circle.

    :param radius: The radius of the circle.
    :return tuple: Area and Circumference of the circle.
    """
    area = pi * radius ** 2
    circumference = 2 * pi * radius

    return area, circumference


def main() -> None:
    r = float(input("Radius: "))
    area, circumference = calc_circle_params(r)
    print(f"Area of circle: {area:.2f}")
    print(f"Circumference of circle: {circumference:.2f}")


if __name__ == '__main__':
    main()