#!/usr/bin/python3

import re


def test_match_with_flag() -> None:
    text = "Ala ma kota a kot ma Ale"
    pattern = "[a-z]{3}"

    print("Test re.match() z flagą re.I:")
    print(f"Tekst: '{text}'")
    print(f"Wzorzec: '{pattern}'")
    print()

    match_without = re.match(pattern, text)
    print(f"Bez flagi re.I: {match_without}")

    match_with = re.match(pattern, text, flags=re.I)
    print(f"Z flagą re.I: {match_with}")
    if match_with:
        print(f"- Dopasowanie: '{match_with.group()}'")
        print(f"- Pozycja: {match_with.span()}")
    print()


def test_search_comparison() -> None:
    text = "Python PYTHON python PyThOn"
    pattern = "python"

    print("Test re.search() - porównanie z flagą i bez:")
    print(f"Tekst: '{text}'")
    print(f"Wzorzec: '{pattern}'")
    print()

    search_without = re.search(pattern, text)
    print(f"Bez flagi: {search_without.group() if search_without else None}")
    if search_without:
        print(f"- Pozycja: {search_without.span()}")

    search_with = re.search(pattern, text, flags=re.I)
    print(f"Z flagą re.I: {search_with.group() if search_with else None}")
    if search_with:
        print(f"- Pozycja: {search_with.span()}")
    print()


def test_findall_comparison() -> None:
    text = "Ala ma kota a kot ma Ale"
    pattern = "ala|ale"

    print("Test re.findall() - porównanie z flagą i bez:")
    print(f"Tekst: '{text}'")
    print(f"Wzorzec: '{pattern}'")
    print()

    findall_without = re.findall(pattern, text)
    print(f"Bez flagi: {findall_without}")

    findall_with = re.findall(pattern, text, flags=re.I)
    print(f"Z flagą re.I: {findall_with}")
    print()


def test_case_sensitive_examples() -> None:
    examples = [
        ("ABC", "[a-z]+", "ABC"),
        ("[A-Z]+", "abc", "abc"),
        ("[a-z]{3}", "Kot", "Kot"),
        ("python", "PYTHON jest super", "PYTHON jest super")
    ]

    print("Dodatkowe przykłady:")
    print("-" * 40)

    for pattern, text, desc in examples:
        print(f"Wzorzec: '{pattern}', Tekst: '{desc}'")

        without = re.search(pattern, text)
        with_flag = re.search(pattern, text, flags=re.I)

        print(f"  Bez flagi: {without.group() if without else 'Brak dopasowania'}")
        print(f"  Z flagą re.I: {with_flag.group() if with_flag else 'Brak dopasowania'}")
        print()


def main() -> None:
    print("=" * 40)
    print("TESTOWANIE FLAGI re.I (IGNORECASE)")
    print("=" * 40)
    print()

    test_match_with_flag()
    print("-" * 40)
    print()

    test_search_comparison()
    print("-" * 40)
    print()

    test_findall_comparison()
    print("-" * 40)
    print()

    test_case_sensitive_examples()
    print("=" * 40)

if __name__ == "__main__":
    main()