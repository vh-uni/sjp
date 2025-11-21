#!/usr/bin/python3

from json import loads, dumps


class A:
    def __init__(self):
        self.l = []
        self.n = 0
        self.s = ""

    def save_data(self):
        try:
            with open("zd9.txt", "w") as f:
                for key, value in self.__dict__.items():
                    f.write(f"{str(key)}={dumps(value)}\n")
        except Exception as e:
            print(e)

    def load_data(self):
        try:
            with open("zd9.txt", "r") as f:
                while line := f.readline():
                    self.__dict__[line.split('=')[0]] = loads(line.split('=')[1].strip())
        except Exception as e:
            print(e)

def main() -> None:
    aa = A()
    aa.n = 15
    aa.l = [1, 2, 3]
    aa.s = "Hello"
    aa.save_data()
    bb = A()
    bb.load_data()
    print(bb.__dict__)


if __name__ == "__main__":
    main()