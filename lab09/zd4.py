#!/usr/bin/python3

import numpy as np


def main() -> None:
    arr = np.arange(1, 13)
    print("Oryginalna tablica:")
    print(arr, end="\n\n")

    reshaped1 = arr.reshape(-1, 2)
    print("Przekształcona tablica (pierwszy parametr -1):")
    print(reshaped1, end="\n\n")

    reshaped2 = arr.reshape(2, -1)
    print("Przekształcona tablica (drugi parametr -1):")
    print(reshaped2, end="\n\n")

if __name__ == "__main__":
    main()