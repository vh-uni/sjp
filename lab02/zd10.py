#!/usr/bin/python3


def main() -> None:
    x = int(input("x = "))
    y = int(input("y = "))
    
    print("\nArithmetic Operations:")
    print(f"x + y = {x + y}")
    print(f"x - y = {x - y}")
    print(f"x * y = {x * y}")

    try:
        print(f"x / y = {x / y}")
        print(f"x // y = {x // y}")
        print(f"x % y = {x % y}")
    except ZeroDivisionError as e:
        print(f"\nError: {e}\n")

    print(f"x ** y = {x ** y}")


if __name__ == '__main__':
    main()