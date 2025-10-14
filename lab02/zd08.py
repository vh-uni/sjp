#!/usr/bin/python3

# Imports
from datetime import date


def main() -> None:
    date_1 = date(2025, 1, 1)
    date_2 = date(2025, 2, 20)
    difference = abs((date_1 - date_2).days)
    print(f"Difference between {date_1} and {date_2} is {difference} day{'' if difference == 1 else 's'}.")


if __name__ == '__main__':
    main()