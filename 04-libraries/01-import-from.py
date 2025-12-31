import random # importing everyting from random module.

coin = random.choice(["heads", "tails"])
print(coin)

""" 
being more specific and not importing everything from a module.
only importing one function
"""
from random import choice

coin = choice(["heads", "tails"])
print(coin)

from random import randint
random_number = randint(0, 9)
print(random_number)