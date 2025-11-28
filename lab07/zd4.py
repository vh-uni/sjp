#!/usr/bin/python3

import re


def main() -> None:
    names = ['Zofia', 'Marek', 'magdalena', 'monika', 'mariusz', 'Zbigniew', 'dariusz', 'Grzegorz', 'Małgorzata', 'Barbara']

    pattern = re.compile(r'^[A-Z].*a$')
    print(list(filter(pattern.match, names)))

if __name__ == "__main__":
    main()