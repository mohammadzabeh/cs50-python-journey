# This script demonstrates how to import a function from your own local module 
# and use it with command-line arguments.

import sys  

# Import the 'hello' function from your own module named 'experimentalModule'
from experimentalModule import hello  

# Check if exactly one command-line argument is provided (excluding the script name)
if len(sys.argv) == 2:
    # Call the hello function with the argument passed from the command line
    hello(sys.argv[1])

