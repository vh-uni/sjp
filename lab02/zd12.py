#!/usr/bin/python3


def main() -> None:
    # a) Integer division operations
    print("a) Division operations with two integers:")
    a, b = 10, 3
    print(f"Numbers: {a} (type: {type(a)}) and {b} (type: {type(b)})")
    print(f"Regular division: {a / b} (type: {type(a / b)})")
    print(f"Integer division: {a // b} (type: {type(a // b)})")
    print(f"Modulo: {a % b} (type: {type(a % b)})")

    # b) Integer and float division operations
    print("\nb) Division operations with integer and float:")
    c, d = 10, 3.0
    print(f"Numbers: {c} (type: {type(c)}) and {d} (type: {type(d)})")
    print(f"Regular division: {c / d} (type: {type(c / d)})")
    print(f"Integer division: {c // d} (type: {type(c // d)})")
    print(f"Modulo: {c % d} (type: {type(c % d)})")

    # c) Float division operations
    print("\nc) Division operations with two floats:")
    e, f = 10.0, 3.0
    print(f"Numbers: {e} (type: {type(e)}) and {f} (type: {type(f)})")
    print(f"Regular division: {e / f} (type: {type(e / f)})")
    print(f"Integer division: {e // f} (type: {type(e // f)})")
    print(f"Modulo: {e % f} (type: {type(e % f)})")


if __name__ == '__main__':
    main()