#!/usr/bin/python3


def main() -> None:
    new_list = []
    print(f"New list: {new_list}")
    for i in range(1, 6):
        new_list.append(i)
    print(f"First and last two elements of list: {new_list[:2] + new_list[-2:]}")
    print(f"Length of list: {len(new_list)}")
    print(f"Even indexes elements: {new_list[::2]}")
    new_list.append(1)
    new_list.append("text")
    # new_list.sort() - TypeError
    new_list.remove("text")  # Or new_list.pop()
    new_list.sort(reverse=True)
    new_list.insert(2, "new element")
    print(f"Count of element '13': {new_list.count(13)}")


if __name__ == '__main__':
    main()