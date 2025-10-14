#!/usr/bin/python3


def reverse_fullname(fullname: str) -> str:
    """
    Reverse the fullname and return it.

    :param fullname: First name and last name.
    :return str: Reversed fullname.
    """

    # Strip unnecessary whitespaces -> Split string by whitespace -> Reverse list of name and surname ->
    # Map title method to each first and last names -> Join list with whitespaces
    return " ".join(map(lambda s: s.title(), reversed(fullname.strip().split(' '))))


def main() -> None:
    fullname = input("Fullname: ")
    print(f"Reversed fullname: {reverse_fullname(fullname)}")


if __name__ == '__main__':
    main()