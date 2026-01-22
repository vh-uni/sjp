#!/usr/bin/python3

import numpy as np


def main() -> None:
    arr = np.random.randint(0, 100, size=(5, 5))
    print("Oryginalna tablica:")
    print(arr, end="\n\n")

    weights = np.array([1, 2, 3, 2, 1])
    weighted_averages = np.average(arr, axis=1, weights=weights)
    print("Średnie ważone dla każdego wiersza:")
    for i, avg in enumerate(weighted_averages):
        print(f"Wiersz {i}: {avg}")


if __name__ == "__main__":
    main()