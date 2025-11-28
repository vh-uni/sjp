#!/usr/bin/python3

import os
import re


def find_files_by_extension(ext_input: str, directory: str = '.') -> list[str]:
    pattern = rf"\.{ext_input}$"

    try:
        files = os.listdir(directory)
        found_files = [f for f in files if re.search(pattern, f, re.IGNORECASE)]

        return found_files

    except FileNotFoundError:
        print("Error: Directory not found.")
    except PermissionError:
        print("Error: Permission denied.")

    return []


def main() -> None:
    files = find_files_by_extension('txt')
    print(f"Files ending in .txt in current directory:")
    for file in files:
        print(f"- {file}")


if __name__ == "__main__":
    main()