#!/usr/bin/python3
import io


def main() -> None:

    try:
        f = open("/sciezka/sciezka/plik.txt", "r")
        print(f.read())  # odczyt całego pliku do końca
        f.close()
    except Exception as e:
        print(e.__class__) # FileNotFoundError

    try:
        f = open("plik.txt", "r")
        f.write("text")
        f.close()
    except Exception as e:
        print(e.__class__) # io.UnsupportedOperation


if __name__ == "__main__":
    main()