#!/usr/bin/python3


def main() -> None:
    try:
        print("32 / x = ?")
        input_string = input("Enter x: ")
        result = 32 / int(input_string)
    except ValueError:
        print("Wrong input")
    except ZeroDivisionError:
        print("You can't divide by zero")
    else:
        print(f"32 / {input_string} = {result}")
    finally:
        print("End of program")


if __name__ == "__main__":
    main()