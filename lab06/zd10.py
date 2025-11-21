#!/usr/bin/python3

import random


def main() -> None:
    try:
        n = int(input("Enter n: "))
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))

        dec_file = "zd10.txt"
        bin_file = "zd10_bin.txt"

        with open(dec_file, "w") as df, open(bin_file, "w") as bf:
            for _ in range(n):
                random_num = random.randint(a, b)
                binary_num = bin(random_num)[2:]

                df.write(str(random_num) + "\n")
                bf.write(binary_num + "\n")

    except Exception as e:
        print(f"Błąd wejścia: {e}")


if __name__ == "__main__":
    main()
