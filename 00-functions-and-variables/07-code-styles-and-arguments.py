def get_name(x, y):
    z = input("hello, my dear, friend. what's your name? ")
    print(x, y, z.strip().title())
get_name("fuck you.", "shut the fuck up. ")
#############################################################
# Short coding style
print("Hi", str(input("name: ")).title().strip())
# Long coding style
g = "name: "
h = str(input(g))
j = h.title()
b = j.strip()
print(g, end=(""))
first, last = b.split(" ")
print("Hello,", first)

