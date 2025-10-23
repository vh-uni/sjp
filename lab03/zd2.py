#!/usr/bin/python3


def main() -> None:
    new_list = []
    while len(new_list) < 10:
        try:
            new_list.append(int(input(f"Enter number ({len(new_list)+1}/10): ")))
        except Exception as e:
            print(f"Error: {e}. Try again.")
            continue

    new_list.sort()
    min_el = new_list[0]
    max_el = new_list[-1]
    print(f"\nThe minimum number is {min_el} and the maximum number is {max_el}.")

    positive_list = list(filter(lambda n: n > 0, new_list))
    print(f"Average of positive numbers: {sum(positive_list) / len(positive_list)}")


if __name__ == '__main__':
    main()