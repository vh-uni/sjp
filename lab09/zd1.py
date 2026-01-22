#!/usr/bin/python3

import numpy as np
from numpy import typing as npt


def replace_zeros(arr: npt.NDArray[int], x: int) -> npt.NDArray[int]:
    return np.where(arr == 0, x, arr)


def main() -> None:
    rows_count = int(input("Podaj liczbę wierszy macierzy: "))
    cols_count = int(input("Podaj liczbę kolumn macierzy: "))

    arr = np.random.randint(low=0, high=10, size=(rows_count, cols_count))
    print("Oryginalna macierz:", arr, sep="\n", end="\n\n")

    x = int(input("Podaj liczbę, na którą mają zostać zamienione zera: "))
    print("")

    result = replace_zeros(arr, x)
    print("Macierz po odjęciu średniej wartości:", result, sep="\n")


if __name__ == "__main__":
    main()