def main():
    name = input("what is your name? ")
    print(hello(name))

def hello(to="World"): 
    """
    If the caller does not pass an argument for to,
    Python automatically uses "world".
    """
    """
    if I only kept print and no return, 
    then this function would not return 
    any value so the test would always fail
    """
    return f"Hello, {to}"


if __name__ == "__main__":
    main()
