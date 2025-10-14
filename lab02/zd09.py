#!/usr/bin/python3

# Imports
import calendar


def main() -> None:
    year = int(input("Year: "))
    month = int(input("Month: "))

    try:
        month_calendar = calendar.month(year, month)
        print('\n' + month_calendar)
    except calendar.IllegalMonthError as e:
        print(f"\nError: {e}\n")

if __name__ == '__main__':
    main()