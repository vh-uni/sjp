#!/usr/bin/python3

from random import randint

def main() -> None:
    list_a = [randint(1, 23) for _ in range(3 + randint(0, 3))]
    list_b = [randint(1, 23) for _ in range(3 + randint(0, 3))]
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")

    list_c = list(list_a)
    list_a[:0] = list_b
    list_b[:0] = list_c
    print(f"First A, then B: {list_b}")
    print(f"First B, then A: {list_a}")


if __name__ == '__main__':
    main()