#!/usr/bin/python3

from random import choice, randint


def main() -> None:
    first_names = [
        "Jan", "Anna", "Piotr", "Katarzyna", "Tomasz",
        "Magdalena", "Marek", "Ewa", "Paweł", "Agnieszka"
    ]

    last_names = [
        "Kowalski", "Nowak", "Wiśniewski", "Wójcik", "Kamiński",
        "Lewandowski", "Zieliński", "Szymański", "Woźniak", "Dąbrowski"
    ]

    grade_sheet = {i: {
        "imie": choice(first_names),
        "nazwisko": choice(last_names),
        "oceny": [randint(1, 5) for _ in range(4 + randint(0, 3))]
    } for i in range(1, 6)}

    for index in grade_sheet:
        print(f"{'-'*5} Student {index} {'-'*5}")
        print(f"Imie: {grade_sheet[index]['imie']}")
        print(f"Nazwisko: {grade_sheet[index]['nazwisko']}")
        print(f"Oceny: {grade_sheet[index]['oceny']}")
        print("\n")


if __name__ == '__main__':
    main()