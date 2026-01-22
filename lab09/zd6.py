#!/usr/bin/python3

import numpy as np


def main() -> None:
    arr = np.random.randint(0, 100, size=10)
    print("Oryginalna tablica:")
    print(arr, end="\n\n")

    sorted_asc = np.sort(arr)
    print("Posortowana tablica rosnąco:")
    print(sorted_asc, end="\n\n")

    sorted_desc = np.sort(arr)[::-1]
    print("Posortowana tablica malejąco:")
    print(sorted_desc, end="\n\n")


if __name__ == "__main__":
    main()