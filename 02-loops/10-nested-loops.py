# building a 2 dimensional Mario block
# 1st approach. my first try.
def main():
    print_square(3)

def print_square(n):
    for _ in range(n):
        print("#" * n)
    
main()

print("=================================================")
# 2nd approach

def main2():
    print_square2(4)

def print_square2(s):
    # for each row in square
    for i in range(s):

        # for each break in row
        for j in range(s):

            # print break
            print("#", end="")
            
        # whenever we have empty print, it types a new line
        print()

    
main2()