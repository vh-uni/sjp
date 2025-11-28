#!/usr/bin/python3


def main() -> None:
    with open('inwokacja.txt', 'r', encoding='utf8') as f:
        content = f.read()

    content = content.replace('.', '...')
    print(content)


if __name__ == "__main__":
    main()