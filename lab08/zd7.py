#!/usr/bin/python3

import re


def fix_capitalization_error(match: re.Match) -> str:
    word = match.group(0)

    if len(word) == 2:
        return word
    else:
        return word[0].upper() + word[1:].lower()


def find_two_letter_errors(text: str) -> list:
    pattern = r'\b[A-Z]{2}\b'
    matches = []
    for match in re.finditer(pattern, text):
        matches.append(match.group(0))
    return matches


def fix_two_letter_with_confirmation(text: str) -> str:
    two_letter_errors = find_two_letter_errors(text)

    if not two_letter_errors:
        return text

    corrections = {}

    for word in two_letter_errors:
        print(f"Wyraz: '{word}'")

        response = input(f"Czy zamienić '{word}' na '{word.lower()}'? (t/n): ").lower()

        if response == 't' or response == 'y':
            corrections[word] = word[0] + word[1].lower()
        else:
            corrections[word] = word

    for original, corrected in corrections.items():
        if original != corrected:
            text = text.replace(original, corrected)

    return text


def auto_fix_capitalization_errors(text: str) -> str:
    pattern = r'\b[A-Za-z](?=[A-Z])(?![A-Z]\b)[A-Za-z]{2,}\b'
    result = re.sub(pattern, fix_capitalization_error, text)

    return result


def find_all_errors(text: str) -> list:
    errors = []

    pattern_long = r'\b[A-Za-z](?=[A-Z])(?![A-Z]\b)[A-Za-z]{2,}\b'
    for match in re.finditer(pattern_long, text):
        errors.append((match.group(0), 'long_word', match.start()))

    # 2-letter uppercase words
    pattern_short = r'\b[A-Z]{2}\b'
    for match in re.finditer(pattern_short, text):
        errors.append((match.group(0), 'short_word', match.start()))

    return sorted(errors, key=lambda x: x[2])


def main() -> None:
    test_text = """
    BYdgoszcz jest miastem w POlsce. Znajduje się tam POlitechnika Bydgoska.
    STudenci uczą się w IT, a także w innych dziedzinach.
    """

    print("Oryginalny tekst:")
    print(test_text)

    errors = find_all_errors(test_text)
    print(f"\nZnaleziono {len(errors)} błędów:")
    for word in errors:
        print(f"- '{word}'")
    print()

    corrected_text = auto_fix_capitalization_errors(test_text)

    print("\nTekst po automatycznej korekcie:")
    print(corrected_text)
    print()

    print("KOREKCJA Z POTWIERDZENIEM:")
    final_text = fix_two_letter_with_confirmation(corrected_text)

    print()
    print("TEKST KOŃCOWY:")
    print(final_text)


if __name__ == "__main__":
    main()