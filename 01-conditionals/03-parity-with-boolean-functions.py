# parity detection

def parity(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")

parity(int(input("x? ")))
#==============================================
def main():
    x = int(input("what's x? "))
    if is_eeeven(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else: 
        return False
# or
def is_eeven(n):
    return True if n % 2 == 0 else False
# or
def is_eeeven(n):
    return n % 2 == 0
    
main()
