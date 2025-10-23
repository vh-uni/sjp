#!/usr/bin/python3


def main() -> None:
    car_dict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "new": False
    }

    car_dict["sold"] = False
    car_dict["new"] = True

    print(f"Car: {car_dict}\n")

    print(f"Pop: {car_dict.pop("year")}")
    print(f"Car: {car_dict}")

    print(f"Pop item: {car_dict.popitem()}")
    print(f"Car: {car_dict}")

    car_dict[6] = 3
    print(f"Car: {car_dict}")


if __name__ == '__main__':
    main()