#!/usr/bin/python3

import numpy as np


def main() -> None:
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])

    print("Tablica 1:")
    print(arr1, end="\n\n")
    print("Tablica 2:")
    print(arr2, end="\n\n")

    elementwise_product = arr1 * arr2
    print("Iloczyn elementów (operator *):")
    print(elementwise_product, end="\n\n")

    matrix_product = arr1 @ arr2
    print("Iloczyn macierzy (operator @):")
    print(matrix_product, end="\n\n")


if __name__ == "__main__":
    main()