"""
Errors: 1. SyntaxError: it is in your code and you have to fix it.
        2. RunTimeError: something is wrong about users input. so
            your code should be prepared for that type of input.

"""


def version_1():
    # you try something.
    try:          
        x  = int(input("what is x? "))
        print(f"x is {x}")
    # anything unexpected happen do this.
    except ValueError:
        print("x is not an integer.")

# you should only try a line of code that you expect errors.
    # so it should be as compact as possible.

# version 2

def version_2(): 
    try: 
        # this code can get errors         
        x  = int(input("what is x? "))
    # anything unexpected happen, do this.
    except ValueError:
        print("x is not an integer.")
    # if the user types any thing except an int,
    # no value would passed to x so we get a name error.
    print(f"x is {x}")


def version_3(): # this one is the standard code.
    # put code that might cause an error.
    try:          
        x  = int(input("what is x? "))   
    # runs if an error happens.
    except ValueError:
        print("x is not an integer.")
    # runs only if no error happened.
    else:
        print(f"x is {x}")


def version_4(): # this way it doesn't break out of the loop
    while True:  # until x is defined
        try:          
            x  = int(input("what is x? "))   
        except ValueError:
            print("x is not an integer.")
        else:
            # print could be here too, no difference in outcome.
            break
            
    print(f"x is {x}")


def version_5(): 
    while True: # same code, more compact.
        try:          
            x  = int(input("what is x? "))   
            break
        except ValueError:
            print("x is not an integer.")

    print(f"x is {x}")

version_5()   