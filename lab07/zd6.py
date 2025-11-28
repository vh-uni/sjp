#!/usr/bin/python3

import re


def identify_phone_pattern(phone_number):
    patterns = {
        "plus_plain": r'^\+\d+$', # Matches: +48123456789
        "zero_plain": r'^00\d+$', # Matches: 0048123456789
        "plus_spaced": r'^\+\d+(?: \d+)+$', # Matches: +48 123 456 789
        "zero_spaced": r'^00\d+(?: \d+)+$', # Matches: 0048 111 222 333
        "plus_dashed": r'^\+\d+(?:-\d+)+$', # Matches: +48-500-600-700
        "zero_dashed": r'^00\d+(?:-\d+)+$', # Matches: 001-202-555-0175
    }

    for pattern_name, regex in patterns.items():
        if re.match(regex, phone_number):
            return pattern_name

    return "invalid"


def main() -> None:
    with open('numery.txt', 'r', encoding='utf-8') as f:
        numbers = [n.strip() for n in f.readlines()]

    number_types = {'plus_plain', 'zero_plain', 'plus_spaced', 'zero_spaced', 'plus_dashed', 'zero_dashed', 'invalid'}
    number_types_counter = {nt: 0 for nt in number_types}

    for num in numbers:
        number_types_counter[identify_phone_pattern(num)] += 1

    for nt in number_types_counter:
        print(f"{nt.title().replace('_', ' ')}: {number_types_counter[nt]}")


if __name__ == "__main__":
    main()