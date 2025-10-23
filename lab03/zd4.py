#!/usr/bin/python3


def main() -> None:
    new_list = [i for i in range(1, 11)]
    print(f"New list: {new_list}")
    odd_elements = list(filter(lambda x: x % 2 == 1, new_list))
    print(f"Odd elements: {odd_elements}")
    print(f"Minimum odd element: {min(odd_elements)}")


if __name__ == '__main__':
    main()