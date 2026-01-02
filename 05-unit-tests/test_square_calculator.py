# testing square calculator program
# these tests are not optimal at all

from square_calculator import square

def main():
    test_square2()

def test_square():
    if square(4) != 16:
        print("4 squared was not 16")
    if square(-7) != 49:
        print("4 squared was not 16")
    if square(0) != 0:
        print("4 squared was not 16")

def test_square2():
    try:
        assert square(4) == 16
    except AssertionError:
        print("4 squared was not 16")
    try:
        assert square(-7) == 49
    except AssertionError:
        print("-7 squared was not 49")



if __name__ == "__main__":
    main()