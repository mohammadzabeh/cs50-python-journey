from random import shuffle

cards = ["A", "B", "C", "D", "E", "F", "G"]
shuffle(cards) # unlike other functions it doesn't return, it shuffles the argument.
i = 1
for card in cards:
    print(f"{i}.", card)
    i += 1

# or

for i, card in enumerate(cards, start = 1):
    print(i, card, sep=". ")
