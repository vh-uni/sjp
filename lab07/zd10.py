#!/usr/bin/python3

import re


def main() -> None:
    words = ["box", "sky", "ant", "apple", "axe", "ray", "six", "owl", "banana", "art"]
    print(f"Words: {words}\n")

    print("Ends with 'x' or 'y':")
    print(list(filter(lambda w: re.search(r"[xy]$", w), words)))

    print("\nThree characters, starts with 'a':")
    print(list(filter(lambda w: re.search(r"^a.{2}$", w), words)))

    print("\nStarts with a vowel:")
    print(list(filter(lambda w: re.search(r"^[aeiou]", w, re.IGNORECASE), words)))


if __name__ == "__main__":
    main()