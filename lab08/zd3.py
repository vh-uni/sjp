#!/usr/bin/python3

import re


def extract_street_name(address: str) -> str:
    match = re.search(r'ul\.\s+([A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]+)', address)
    return match.group(1) if match else None


def extract_postal_code(address: str) -> str:
    match = re.search(r'\b(\d{2}-\d{3})\b', address)
    return match.group(1) if match else None


def extract_apartment_number(address: str) -> str:
    match = re.search(r'\b\d+/(\d+)\b', address)
    return match.group(1) if match else None


def main() -> None:
    with open('adresy.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    lines = text.strip().split('\n')

    for i, line in enumerate(lines, 1):
        print(f"Adres {i}: {line}")

        street = extract_street_name(line)
        postal_code = extract_postal_code(line)
        apartment = extract_apartment_number(line)

        print(f"Nazwa ulicy: {street}")
        print(f"Kod pocztowy: {postal_code}")
        print(f"Numer mieszkania: {apartment if apartment else 'Brak'}")
        print("-" * 15)


if __name__ == "__main__":
    main()