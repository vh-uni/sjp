#!/usr/bin/python3


def main() -> None:
    with open('inwokacja.txt', 'r', encoding='utf8') as f:
        content = f.read()

    print(f'Amount of new lines: {content.count("\n")}')
    print(f'Amount of spaces: {content.count(" ")}')
    print(f'Amount of tabs: {content.count("\t")}')


if __name__ == "__main__":
    main()