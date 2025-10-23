#!/usr/bin/python3

from random import randint

def main() -> None:
    list_a = [randint(1, 23) for _ in range(5 + randint(0, 5))]
    list_b = [randint(1, 23) for _ in range(5 + randint(0, 5))]
    print(f"List a: {list_a}")
    print(f"List b: {list_b}")
    print(f"Unique elements of list a: {set(list_a).difference(set(list_b))}")


if __name__ == '__main__':
    main()