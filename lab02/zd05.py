#!/usr/bin/python3

# Constants and Global variables
a: str = "Global variable"
A: str = "Global constant"


def example_function() -> None:
    a = "Local variable"

    print(f"A in example_function(): {A} | type: {type(A)}")
    print(f"a in example_function(): {a} | type: {type(a)}")



def main() -> None:
    example_function()


if __name__ == '__main__':
    main()