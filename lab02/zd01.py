#!/usr/bin/python3

# Imports
from typing import Optional

# Constants and Global variables
GREETING: str = "Hello"
addressee: str = "world"


# Greeting function
def hello_func(hello_to: Optional[str] = "Python") -> None:
    """
    Display greeting.

    :param hello_to: Optional greeting addressee.
    :return None:
    """
    print(f"{GREETING}, {hello_to}!")


# Main function
def main() -> None:
    hello_func(addressee)


if __name__ == '__main__':
    main()