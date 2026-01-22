#!/usr/bin/python3

import numpy as np


def main() -> None:
    arr = np.random.randint(0, 10, size=(10, 10))
    print("Oryginalna tablica:")
    print(arr, end="\n\n")

    num, counts = np.unique(arr, return_counts=True)
    print("Liczność wystąpień elementów:")
    for value, count in zip(num, counts):
        print(f"Wartość {value}: {count} razy")


if __name__ == "__main__":
    main()