#!/usr/bin/python3

import re


def main() -> None:
    email_pattern = r'^[a-z][a-z0-9_.-]*@gmail\.com$'

    email = input("Enter your gmail address: ").strip()
    if re.match(email_pattern, email):
        print("Valid Gmail address.")
    else:
        print("Invalid Gmail address.")


if __name__ == "__main__":
    main()