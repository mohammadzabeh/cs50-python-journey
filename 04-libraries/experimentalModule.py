def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Good Bye, {name}")

# The following if-statement checks if this file is being run directly (not imported as a module)
# When Python runs a script, it sets a special variable __name__.
# If this script is the main program being executed, __name__ will be "__main__".
# This condition ensures that main() is called only when the script is run directly,
# and prevents it from running if the script is imported into another file.
if __name__ == "__main__":
    main()
