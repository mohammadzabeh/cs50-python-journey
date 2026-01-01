# command line arguments
# sys module: 
"""The sys module provides access to interpreter-level
variables and functions, letting you interact directly with the 
Python runtime environment (e.g., command-line arguments, 
exit control, and system paths)."""
# sys.argv
"""sys.argv is a list that contains the command-line arguments passed 
to a Python script, where the first element is the script’s filename."""

import sys

# here you can type your name after fileName.py and it prints:
# hello, my name is yourName
def version_1():
    print("hello, my name is", sys.argv[1]) # 0 is the fileName.py

# handling indexError. if the user forget to type their name
def version_2():
    try:
        name = sys.argv[1]
    except IndexError: 
        print("type your name.")
    else:   
        print("hello, my name is", name)

def version_3():
    if len(sys.argv) < 2:
        print("Too few arguments")
    elif len(sys.argv) > 2:
        print("Too many arguments")
    else:
        print("hello, my name is", sys.argv[1])

# is you type "python file.py David Malan" you get too many arguments but
# if you put David Malan in quotations it recognizes it as one argument.

# this version is the same. it's better to seperate the main code from the
# error handling lines.
def version_4():
    # check for errors
    if len(sys.argv) < 2:
        # exit will end the program, because if we don't, we'll have an indexError line 48
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    # print name tags
    print("hello, my name is", sys.argv[1])

def version_5():
    if len(sys.argv) < 2:
        sys.exit("too few arguments")
    for arg in sys.argv[1:]: # this gives you a slice of a list from 1 to the end of the list
        print("Hello, my name is", arg)

# [1:-1] this slice will give you 1 to the end except the last one

version_5()