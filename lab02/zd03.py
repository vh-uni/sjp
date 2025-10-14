#!/usr/bin/python3

# Imports
from datetime import datetime as dt


def display_time() -> None:
    """
    Display current time.

    :param:
    :return None:
    """
    print(dt.now().strftime("%A, %B %d, %Y"))
    print(dt.now().strftime("%d.%m.%Y, %H:%M:%S"))
    print(dt.now().strftime("%m/%d/%Y, %I:%M:%S %p"))


def main() -> None:
    display_time()


if __name__ == '__main__':
    main()