#!/usr/bin/python3


def main() -> None:
    the_set =   {"orange", "banana", "apple", "cherry", "kiwi"}
    print(f"The set is: {the_set}")
    # the_set.remove("bananaa") - KeyError
    the_set.discard("bananaa") # - No Error
    print(f"The set is: {the_set}\n")

    print(f"Pop element: {the_set.pop()}")
    print(f"Pop element: {the_set.pop()}")
    print(f"Pop element: {the_set.pop()}")
    print(f"The set is: {the_set}")


if __name__ == '__main__':
    main()