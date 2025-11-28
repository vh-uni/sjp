#!/usr/bin/python3

import re


def main() -> None:
    with open('numery.txt', 'r', encoding='utf-8') as f:
        numbers = f.readlines()

    polish_pattern = re.compile(r'^(\+48|0048)')
    polish_numbers = [n.strip() for n in filter(polish_pattern.match, numbers)]
    print(polish_numbers)


if __name__ == "__main__":
    main()