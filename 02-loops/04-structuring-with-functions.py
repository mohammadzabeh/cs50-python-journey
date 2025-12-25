def main():
    number = get_number()
    meow(number)

def get_number():
    while True: 
        n = int(input("what's n? "))
        if n > 0:
            break  # instead of break we could only use
    return n       # return, it breaks and returns a value.

def meow(n):
    for _ in range(n):
        print("meaw")

main()
