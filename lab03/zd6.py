#!/usr/bin/python3


def main() -> None:
    new_list = []
    user_input = input("Enter a number: ")
    while user_input != "0":
        try:
            new_list.append(int(user_input))
        except Exception as e:
            print(f"Error: {e}. Try again.")

        user_input = input("Enter a number: ")

    print(f"New list: {new_list}")
    print(f"Unique elements of list: {set(new_list)}")


if __name__ == '__main__':
    main()