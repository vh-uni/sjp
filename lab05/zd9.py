#!/usr/bin/python3


def power_of_two(exponent: int) -> int:
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")

    return 1 << exponent


def main() -> None:
    print("2^p = 1 << p")

    try:
        user_input = input("\nEnter exponent p to calculate 2^p: ")

        if user_input.strip():
            exponent = int(user_input)
            result = power_of_two(exponent)
            print(f"2^{exponent} = {result}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()