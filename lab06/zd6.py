#!/usr/bin/python3

import os


def print_dir_tree(path, level = 0):
    try:
        for element in os.listdir(path):
            full_path = os.path.join(path, element)
            print("|\t" * level + "|-" + element)
            if os.path.isdir(full_path):
                print_dir_tree(full_path, level + 1)
    except PermissionError:
        print("|\t" * level + "|_ [No permission]")


def main() -> None:
    print_dir_tree(os.getcwd())


if __name__ == "__main__":
    main()