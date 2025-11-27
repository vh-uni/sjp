#!/usr/bin/python3


def main() -> None:
    with open("plik_w.txt", "w") as f:
        f.write("Zapis w trybie 'w'") # Overwrite content of file

    with open("plik_a.txt", "a") as f:
        f.write("Dopisano w trybie 'a'") # Append content to the end of a file

    try:
        with open("plik_x.txt", "x") as f:
            f.write("Utworzono w trybie 'x'") # Only create new file with provided content
    except FileExistsError:
        print("Plik już istnieje – nie można utworzyć ponownie")


if __name__ == "__main__":
    main()