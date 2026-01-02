# making a calc to test it in another python file

def main():
    number = get_number()
    squared_number = square(number)
    print(f"{squared_number:,}")

def get_number():
    x = int(input("what's x? "))
    return x

def square(n):
    return n * n

if __name__ == "__main__":
    main()