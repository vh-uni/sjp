#!/usr/bin/python3


def main() -> None:
    with open('inwokacja.txt', 'r', encoding='utf8') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    lines_amount = len(lines)
    print(f'Amount of lines: {lines_amount}')

    words_amount_sum = 0
    chars_amount_sum = 0
    for i, line in enumerate(lines, start=1):
        words = line.split()
        words_amount = len(words)
        chars_amount = len(line)
        print(f'Line {i}: {chars_amount} characters and {words_amount} words')

        words_amount_sum += words_amount
        chars_amount_sum += chars_amount

    print(f'Total amount of words: {words_amount_sum}')
    print(f'Total amount of characters: {chars_amount_sum}')

if __name__ == "__main__":
    main()