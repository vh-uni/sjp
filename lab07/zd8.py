#!/usr/bin/python3

import re
import calendar
from datetime import datetime


def validate_date(date_input: str) -> None:
    pattern = r"^(0[1-9]|[12][0-9]|3[01])([-/.])(0[1-9]|1[0-2])\2\d{4}$"
    match = re.match(pattern, date_input)

    if match:
        try:
            sep = match.group(2)
            date_obj = datetime.strptime(date_input, f"%d{sep}%m{sep}%Y")

            print(f"Valid date. Month: {calendar.month_name[date_obj.month]}")

        except ValueError:
            print("Date does not exist in calendar.")
    else:
        print("Invalid format.")


def main() -> None:
    date_input = input("Enter date (dd-mm-yyyy, dd/mm/yyyy, or dd.mm.yyyy): ")
    validate_date(date_input)


if __name__ == "__main__":
    main()