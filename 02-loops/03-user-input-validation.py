while True:
    n = int(input("n? "))
    if n < 0:
        continue
    else:
        print("meaw\n" * n, end="")
        break
        
# or 

while True:
    n = int(input("n? "))
    if n > 0:
        break

for _ in range(n):
    print("meaww")

