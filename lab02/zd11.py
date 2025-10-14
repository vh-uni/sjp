#!/usr/bin/python3


def main() -> None:
    # a) Testing multiplication and division order (left-to-right)
    print("a) Multiplication and division order:")
    result_a = 10 / 2 * 3  # First 10/2=5, then 5*3=15
    print(f"10 / 2 * 3 = {result_a}")  # Should be 15

    # b) Testing multiplication vs addition priority
    print("\nb) Multiplication vs addition:")
    result_b1 = 2 + 3 * 4  # First 3*4=12, then 2+12=14
    result_b2 = (2 + 3) * 4  # First 2+3=5, then 5*4=20
    print(f"2 + 3 * 4 = {result_b1}")
    print(f"(2 + 3) * 4 = {result_b2}")

    # c) Testing parentheses effect
    print("\nc) Parentheses effect:")
    result_c1 = 10 - 2 + 3  # Left to right: 10-2=8, then 8+3=11
    result_c2 = 10 - (2 + 3)  # First 2+3=5, then 10-5=5
    print(f"10 - 2 + 3 = {result_c1}")
    print(f"10 - (2 + 3) = {result_c2}")

    # d) Testing multiplication vs exponentiation
    print("\nd) Multiplication vs exponentiation:")
    result_d1 = 2 * 3 ** 2  # First 3**2=9, then 2*9=18
    result_d2 = (2 * 3) ** 2  # First 2*3=6, then 6**2=36
    print(f"2 * 3 ** 2 = {result_d1}")
    print(f"(2 * 3) ** 2 = {result_d2}")


if __name__ == '__main__':
    main()