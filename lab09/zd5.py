#!/usr/bin/python3

import numpy as np


def main() -> None:
    data = np.loadtxt('oceny.csv', skiprows=1)
    lab_grades = data[:, :-1]
    exam_grades = data[:, -1]

    min_lab_grades = np.min(lab_grades, axis=1)
    avg_exam_grade = np.mean(exam_grades)
    avg_lab_grades = np.mean(lab_grades, axis=1)
    two_exam_grades = np.sum(exam_grades == 2)
    has_all_fives = np.any(np.all(lab_grades == 5, axis=1))
    has_twos_lab2_lab3 = np.any((lab_grades[:, 1] == 2) & (lab_grades[:, 2] == 2))
    exam_higher_avg_lab = np.sum(exam_grades > avg_lab_grades)
    num_most_fives = np.max(np.sum(lab_grades == 5, axis=1))

    print("Najniższe oceny z laboratoriów dla każdego studenta:")
    for i, grade in enumerate(min_lab_grades):
        print(f"Student {i + 1}: {grade}")

    print(f"\nŚrednia ocena z egzaminu: {avg_exam_grade}")
    print(f"Liczba 2 z egzaminu: {two_exam_grades}")
    print(f"Czy jest student, który miał same 5 z laboratoriów? {'Tak' if has_all_fives else 'Nie'}")
    print(f"Czy jest student, który miał 2 z LAB2 i LAB3? {'Tak' if has_twos_lab2_lab3 else 'Nie'}")
    print(f"Liczba studentów, którzy dostali wyższą ocenę z egzaminu niż ich średnia ocen z laboratoriów: {exam_higher_avg_lab}")
    print(f"Liczba piątek, którą uzyskał student mający najwięcej 5 w całej grupie: {num_most_fives}")


if __name__ == "__main__":
    main()