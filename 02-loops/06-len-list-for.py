# using len, for, range to rank the objects.
students = ["Alex", "Ali", "David"]

for i in range(len(students)): 
    # range expects an int so we use len to get the length. 
    print(i + 1, students[i])
