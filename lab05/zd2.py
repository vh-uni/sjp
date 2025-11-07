#!/usr/bin/python3

def get_value_of_bit(index: int, number: int) -> int:
    bin_number = bin(number).split("b")[1]

    if len(bin_number) == 1:
        return int(bin_number[0])
    else:
        return int(bin_number[-(index+1)])


def main() -> None:
    try:
        number = int(input("Enter a decimal number from 0 to 255: "))
        if number not in range(0, 256):
            raise ValueError(f"number {number} is not in the range of 0 to 255")

        bit_index = int(input("Enter a bit index: "))
        if bit_index not in range(0, len(bin(number).split("b")[1])):
            raise ValueError(f"bit index is out of binary number length")
    except ValueError as e:
        print(f"Wrong input: {e}")
        exit(1)

    print(f"\nBinary representation of a: {bin(number).split("b")[1]}")
    print(f"Value of a bit {bit_index}: {get_value_of_bit(bit_index, number)}")



if __name__ == "__main__":
    main()