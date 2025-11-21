#!/usr/bin/python3

import shutil
import os


def main() -> None:
    try:
        copy_path = os.path.join("copy_dir", "plik_a.txt")
        shutil.copy("plik_a.txt", copy_path)
    except Exception as e:
        print(e) # file is successfully copied

    try:
        copy_path = os.path.join("copy_dir", "plik_w.txt")
        shutil.copy("plik_a.txt", copy_path) # overwrite file in target directory
    except Exception as e:
        print(e)

    try:
        copy_path = os.path.join("no_dir", "plik_a.txt")
        shutil.copy("plik_a.txt", copy_path) # No such file or directory: ...
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()