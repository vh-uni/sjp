#!/usr/bin/python3

import math
import sys


def test_rounding_functions(number: float) -> None:
    # math.trunc() - truncates towards zero (removes decimal part)
    trunc_result = math.trunc(number)
    print(f"math.trunc({number}) = {trunc_result}")

    # math.floor() - rounds down to nearest integer
    floor_result = math.floor(number)
    print(f"math.floor({number}) = {floor_result}")

    # math.ceil() - rounds up to nearest integer
    ceil_result = math.ceil(number)
    print(f"math.ceil({number}) = {ceil_result}")

    print(f"trunc: {trunc_result}, floor: {floor_result}, ceil: {ceil_result}")

    # For positive numbers: trunc = floor
    # For negative numbers: trunc = ceil


def test_lcm_gcd(a: int, b: int) -> None:
    # math.gcd() - Greatest Common Divisor
    gcd_result = math.gcd(a, b)
    print(f"math.gcd({a}, {b}) = {gcd_result}")

    # math.lcm() - Least Common Multiple (Python 3.9+)
    lcm_result = math.lcm(a, b)
    print(f"math.lcm({a}, {b}) = {lcm_result}")

    # Verify the relationship: a * b = gcd(a, b) * lcm(a, b)
    product_ab = abs(a * b)
    product_gcd_lcm = gcd_result * lcm_result

    print()
    print(f"Verification:")
    print(f"|a * b| = {product_ab}")
    print(f"gcd(a,b) * lcm(a,b) = {product_gcd_lcm}")
    print()
    print(f"{'Correct!' if product_ab == product_gcd_lcm else 'Error!'}", end="\n\n")


def check_python_version() -> tuple:
    version_info = sys.version_info
    major = version_info.major
    minor = version_info.minor
    micro = version_info.micro

    print(f"Full version: {sys.version}")
    print(f"Version: {major}.{minor}.{micro}")
    print(f"Version info: {version_info}")

    return major, minor, micro


def main() -> None:
    major, minor, micro = check_python_version()

    print()

    try:
        user_input = input("Enter float variable 'a': ")
        print()
        test_rounding_functions(float(user_input))
    except ValueError as e:
        print(f"Invalid input - {e}")

    print()

    # Math absolute value function
    print(math.fabs(-5.7))
    print(math.fabs(3.2))

    print()

    if major > 3 or (major == 3 and minor >= 9):
        print(f"Python version {major}.{minor} supports math.lcm() and math.gcd()")

        test_pairs = [(12, 18), (24, 36)]
        for a, b in test_pairs:
            test_lcm_gcd(a, b)
    else:
        print(f"Python version {major}.{minor} does not support math.lcm() and math.gcd()")


if __name__ == "__main__":
    main()