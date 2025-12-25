# int things
def division():
    x = float (input("first number: "))
    y = float(input("second number: "))
    z = round(x / y, 3)
    z = f"{z:.2f}"
    print(z)
#==============================================
def main():
    x = int(input("number: "))
    print("squared number:,", square(x))

def square(n):
    return n * n


main()