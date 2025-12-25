# 1. making a calculator 1.
x = int(input("1. what's x? ").strip())
y = int(input("what's y? ").strip())
print(x + y)
# 2. making a calculator 2 (not readable enough).
print(int(input("2. what's x? ")) + int(input("what's y? ")))
# 3. a calc that can read float.
x = float(input("3. what's x? ").strip())
y = float(input("what's y? ").strip())
print(x + y)
# 4. a calc that rounds the float number
x = float(input("4. what's x? ").strip())
y = float(input("what's y? ").strip())
print(round(x + y))
# 5. a calc the uses , for seperating large numbers.
x = int(input("5. what's x? "))
y = int(input("what's y? "))
z = x + y
print(f"{z:,}")
# 6. division with rounding the a specific decimal.
x = float(input("6. what's x? "))
y = float(input("what's y? "))
z = x / y
z = round(z, 2)
print(z)
# 7. same thing using f string
x = float(input("7. what's x? "))
y = float(input("what's y? "))
z = x / y
print(f"{z:.2f}")
