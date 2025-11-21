#!/usr/bin/python3

import random


def generate_random_nums(n: int, a: int, b: int) -> None:
    for i in range(n):
        random_num = random.randint(a, b)

        try:
            with open("zd8.txt", "a") as file:
                file.write(str(random_num) + "\n")
        except FileNotFoundError:
            with open("zd8.txt", "w") as file:
                file.write(str(random_num) + "\n")


def main() -> None:
    n = input("Enter n: ")
    a = input("Enter a: ")
    b = input("Enter b: ")

    try:
        generate_random_nums(int(n), int(a), int(b))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()