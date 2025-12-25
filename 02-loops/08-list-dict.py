# so we are creating a list of dictionaries.

students = [
    {"name": "Alex", "university": "Harvard", "city": "New York"},
    {"name": "Sam", "university": "Prinston", "city": "chicago"},
    {"name": "Rob", "university": None, "city": "Dallas"}, # this one doesn't go to uni so we use None keyword.
    {"name": "Derek", "university": "Massachusetts Institute of Technology", "city": "Los Angeles"}
    ]

for student in students:
    print(student)
    # this will print each curly brace.


for student in students:
    print(student["name"])
    # this calls only the value associated with the name.

for student in students:
    print(student["name"], student["university"], student["city"], sep=", ")
    