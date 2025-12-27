def main():
    x = get_int4("what's x? ")
    print(f"x is {x}")

def get_int1():
    while True: 
        try:          
            x  = int(input("what is x? "))  
            return x 
        except ValueError:
            print("x is not an integer.")

def get_int2():   # trying to make it as compact as possible.
    while True: 
        try:          
            return int(input("what is x? "))   
        except ValueError:
            print("x is not an integer.")

def get_int3():  
    """using pass keyword. it still proccess the
        error but passes to continue to loop.""" 
    while True: 
        try:          
            return int(input("what is x? (x should be an intejer!) "))   
        except ValueError:
            pass

def get_int4(prompt):  
    """maybe it's better to give our function a variable.
        so that that we know what main wants.""" 
    while True: 
        try:          
            return int(input(prompt))   
        except ValueError:
            pass
            
main()