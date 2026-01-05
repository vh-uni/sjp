#!/usr/bin/python3

import re


def main() -> None:
    with open('inwokacja.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    print("Słowa, po których występuje '!':")
    words_excl = re.findall(r'\b\w+(?=!)', text)
    print(words_excl)
    print(f"Liczba: {len(words_excl)}\n")

    print("Słowa z polskimi znakami:")
    polish_words = re.findall(r'\b\w*[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]\w*\b', text)
    print(polish_words)
    print(f"Liczba: {len(polish_words)}\n")

    print("Wystąpienia 'cię'/'ci':")
    count = len(re.findall(r'\bci[eę]?\b', text, re.IGNORECASE))
    print(f"Liczba wystąpień: {count}")


if __name__ == "__main__":
    main()
