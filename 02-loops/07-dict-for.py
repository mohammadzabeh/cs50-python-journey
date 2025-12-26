# dictionaries, dict and etc
students = {"Alex": "Harvard", # we press Enter after
            "David": "Harvard",#    each line for syntax clarity.
            "Sam": "Cambridge", 
            "Simon": "Babbel"}
# here in this example Alex is a key and the value
#   associated with is Harward.
print(students["Alex"])  
# here we get Harward.
# previously we used lists and we used a number for
# calling an object.

for student in students:
    print(student)
# this gives us only the keys

for student in students:
    print(student, students[student], sep=", ")
# so first the key and secont the value associated.
# using sep=", " for better readability. we can use 
# sep="\n"

for student in students:
    number_of_spaces = 20 - len(student) 
    print(student, students[student], sep=" " * number_of_spaces)
# I used len and sep=" " to have the values alined below each other.

