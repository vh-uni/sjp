#!/usr/bin/python3

import numpy as np
from numpy import typing as npt


def meadianize(arr: npt.NDArray[int]) -> npt.NDArray[float]:
    mean_value = np.mean(arr)
    print(f"Średnia wartość macierzy: {mean_value}\n")
    return (arr - mean_value).astype(float) # astype to ensure arrays of floats, for annotation purposes


def main() -> None:
    rows_count = int(input("Podaj liczbę wierszy macierzy: "))
    cols_count = int(input("Podaj liczbę kolumn macierzy: "))

    arr = np.random.randint(low=0, high=10, size=(rows_count, cols_count))
    print("Oryginalna macierz:", arr, sep="\n", end="\n\n")

    result = meadianize(arr)
    print("Macierz po odjęciu średniej wartości:", result, sep="\n")


if __name__ == "__main__":
    main()