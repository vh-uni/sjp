#!/usr/bin/python3

import numpy as np


def main() -> None:
    arr = np.random.randint(0, 100, size=(5, 5))
    print("Macierz:")
    print(arr, end="\n\n")

    global_max = np.max(arr)
    print(f"Element największy globalnie: {global_max}", end="\n\n")

    row_maxes = np.max(arr, axis=1)
    print("Elementy największe w każdym wierszu:")
    for i, value in enumerate(row_maxes):
        print(f"Wiersz {i}: {value}")

    print("")

    col_maxes = np.max(arr, axis=0)
    print("Elementy największe w każdej kolumnie:")
    for i, value in enumerate(col_maxes):
        print(f"Kolumna {i}: {value}")


if __name__ == "__main__":
    main()