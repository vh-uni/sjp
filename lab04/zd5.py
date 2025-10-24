#!/usr/bin/python3


class Item:
    def get_sound(self) -> None:
        print("item's sound")


class Element:
    def get_sound(self) -> None:
        print("element's sound")


# If multiple parent classes define a method with the same name, the method from the first parent class is used.
class Thing(Item, Element):
    def say_hello(self) -> None:
        print("hello!")


def main():
    i = Item()
    i.get_sound()

    e = Element()
    e.get_sound()

    t = Thing()
    t.get_sound()

if __name__ == "__main__":
    main()