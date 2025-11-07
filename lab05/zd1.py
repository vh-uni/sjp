#!/usr/bin/python3

def get_numeral_system() -> int:
    numeral_systems = (2, 8, 10, 16)
    inp = input("Input the numeral system: ")

    if inp.isdigit() and int(inp) in numeral_systems:
        return int(inp)
    else:
        print(f"Numeral system must be one of {numeral_systems}")
        return get_numeral_system()


def main() -> None:
    numeral_system = get_numeral_system()
    a = int(input("Input value of a: "), numeral_system)

    print(f"Binary representation of a: {bin(a)}")
    print(f"Octal representation of a: {oct(a)}")
    print(f"Decimal representation of a: {int(a)}")
    print(f"Hexadecimal representation of a: {hex(a)}")


if __name__ == "__main__":
    main()