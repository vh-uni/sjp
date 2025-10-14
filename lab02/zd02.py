#!/usr/bin/python3

# Imports
import sys


def display_version() -> None:
    """
    Display python version.

    :param:
    :return None:
    """
    print(f"Current python version: {sys.version}")


def main() -> None:
    display_version()


if __name__ == '__main__':
    main()