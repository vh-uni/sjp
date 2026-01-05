#!/usr/bin/python3

import re


def extract_street_name_advanced(address: str) -> str:
    match = re.search(r'(?:ul\.|Al\.|Aleja|Ulica)\s+((?:(?:prof\.|dr\.|św\.|gen\.|mjr\.)\s+)?(?:[A-ZĄĆĘŁŃÓŚŹŻ]\.?\s*)*[A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]+(?:\s+[A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]+)*)\s+(?=\d)', address)
    return match.group(1).strip() if match else None


def main() -> None:
    with open('adresy.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    lines = text.strip().split('\n')

    for addr in lines:
        advanced = extract_street_name_advanced(addr)
        print(f"Nazwa ulicy: {advanced}")


if __name__ == "__main__":
    main()