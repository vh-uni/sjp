#!/usr/bin/python3

import re


def main() -> None:
    print(re.findall('a+', 'aaaa'))
    print(re.findall('a*', 'aaaa'))
    print(re.findall('a?', 'aaaa'))
    print(re.findall('a+?', 'aaaa'))
    print(re.findall('a*?', 'aaaa'))
    print(re.findall('a??', 'aaaa'))


if __name__ == "__main__":
    main()
