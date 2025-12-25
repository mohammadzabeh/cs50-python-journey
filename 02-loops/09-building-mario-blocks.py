# building blocks on each other like mario game.
# 1st approach
print("#")
print("#")
print("#")

# 2nd approach

for i in range(3):
    print("#")

# 3nd approach

def main():
    print_column(hight)

hight = int(input("what's the hight? "))

def print_column(h):
    for _ in range(hight):
        print("#")
    print("#\n" * hight, end="")   # or this instead of for.

main()

# 4th approach a row

def main2():
    print_row(width)

width = int(input("what's the width? "))
def print_row(l):
    print("?" * width)

main2()