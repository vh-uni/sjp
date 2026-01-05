#!/usr/bin/python3

import re


def is_weak_password(password: str) -> bool:
    pattern = r'^.{6,}$'
    return bool(re.match(pattern, password))


def is_medium_password(password: str) -> bool:
    pattern = r'^(?=.*[a-z])(?=(?:.*[A-Z])|(?:.*\d)).{8,}$'
    return bool(re.match(pattern, password))


def is_strong_password(password: str) -> bool:
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_#\-+.]).{12,}$'
    return bool(re.match(pattern, password))


def check_password_strength(password: str) -> str:
    if is_strong_password(password):
        return 'strong'
    elif is_medium_password(password):
        return 'medium'
    elif is_weak_password(password):
        return 'weak'
    else:
        return 'too weak'


def get_password_details(password: str) -> dict:
    return {
        'length': len(password),
        'has_lowercase': bool(re.search(r'[a-z]', password)),
        'has_uppercase': bool(re.search(r'[A-Z]', password)),
        'has_digit': bool(re.search(r'\d', password)),
        'has_special': bool(re.search(r'[@$!%*?&_#\-+.]', password))
    }


def main() -> None:
    test_passwords = [
        "abc",
        "abc123",
        "password",
        "Password",
        "Password1",
        "Pass1234",
        "MyPassword123",
        "MyPass123!",
        "MyP@ssw0rd123",
        "Str0ng!Pass",
        "VeryStr0ng!P@ss",
        "Sup3r$ecure#2024",
    ]

    print("KRYTERIA:")
    print("- SŁABE (weak): Co najmniej 6 znaków")
    print("- ŚREDNIE (medium): Co najmniej 8 znaków + małe litery + (wielkie ALBO cyfry)")
    print("- MOCNE (strong): Co najmniej 12 znaków + małe + wielkie + cyfry + znaki specjalne")
    print()

    for password in test_passwords:
        strength = check_password_strength(password)
        details = get_password_details(password)

        print(f"Hasło: '{password}'")
        print(f"- Siła: {strength.upper()}")
        print(f"- Długość: {details['length']}")
        print(f"- Małe litery: {'+' if details['has_lowercase'] else '-'},", end="  ")
        print(f"Wielkie litery: {'+' if details['has_uppercase'] else '-'},", end="  ")
        print(f"Cyfry: {'+' if details['has_digit'] else '-'},", end="  ")
        print(f"Znaki specjalne: {'+' if details['has_special'] else '-'}")
        print()


if __name__ == "__main__":
    main()