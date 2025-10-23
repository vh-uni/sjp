#!/usr/bin/python3


def main() -> None:
    set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    set_b = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

    print(f"Set a: {set_a}")
    print(f"Set b: {set_b}")

    print("\n")

    print(f"Is A disjoint B: {set_a.isdisjoint(set_b)}")
    print(f"Is A subset B: {set_a.issubset(set_b)}")
    print(f"Is A superset B: {set_a.issuperset(set_b)}")
    print(f"A union B: {set_a.union(set_b)}")
    print(f"A difference B: {set_a.difference(set_b)}")
    print(f"A intersection B: {set_a.intersection(set_b)}")


if __name__ == '__main__':
    main()