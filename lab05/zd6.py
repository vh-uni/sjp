#!/usr/bin/python3

import math


def calculate_ladder_height(length: float, angle_degrees: float) -> float:
    angle_radians = math.radians(angle_degrees)
    height = length * math.sin(angle_radians)
    return height


def main() -> None:
    print("Ladder Height Calculator")
    print("=" * 40)

    try:
        length = float(input("Enter ladder length (in meters): "))

        if length <= 0:
            print("Ladder length must be greater than zero!")
            return

        angle = float(input("Enter angle relative to the horizontal (in degrees): "))

        if angle < 0 or angle > 90:
            print("Angle must be between 0 and 90 degrees!")
            return

        height = calculate_ladder_height(length, angle)

        print(f"\nA ladder with length {length} m")
        print(f"inclined at an angle of {angle}° from the horizontal")
        print(f"reaches a height of: {height:.2f} m")

    except ValueError:
        print("Please enter a valid number!")


if __name__ == "__main__":
    main()