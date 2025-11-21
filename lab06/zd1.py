#!/usr/bin/python3


def test_func1(input_string):
    try:
        some_number = 3 / 0
        # some_number = float(input_string)
        # some_number = float(input_string)
        print(f"This number is: {some_number}")
    except (ValueError, UnicodeError) as ex1:
        print("cannot do it :(")
        print(ex1)
    except NameError:
        print("i dont know this name :(")
    except:
        print("i dont know this error, sorry..")


def test_func2(input_string):
    try:
        # some_number = 3 / 0
        some_number = float(input_string)
        # some_number = float(input_string)
        print(f"This number is: {some_number}")
    except (ValueError, UnicodeError) as ex1:
        print("cannot do it :(")
        print(ex1)
    except NameError:
        print("i dont know this name :(")
    except:
        print("i dont know this error, sorry..")


def test_func3(input_string):
    try:
        # some_number = 3 / 0
        # some_number = float(input_string)
        some_number = float(inputt_string)
        print(f"This number is: {some_number}")
    except (ValueError, UnicodeError) as ex1:
        print("cannot do it :(")
        print(ex1)
    except NameError:
        print("i dont know this name :(")
    except:
        print("i dont know this error, sorry..")



def main() -> None:
    input_string = "2,5"
    test_func1(input_string)
    test_func2(input_string)
    test_func3(input_string)



if __name__ == "__main__":
    main()