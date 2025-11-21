#!/usr/bin/python3


def main() -> None:
    x = -1

    try:
        if x < 0:
            raise Exception("Sorry, no numbers below zero")
    except Exception as e:
        print(e)

    try:
        if x < 0:
            raise ValueError("Sorry, no numbers below zero")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()