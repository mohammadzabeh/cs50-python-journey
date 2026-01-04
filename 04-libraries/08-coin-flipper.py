"""
***01-coin-flipper.py***
Create a program that simulates flipping a coin multiple times.
 Ask the user how many times to flip, 
 then show the count of heads and tails. Use random.choice().
"""
from random import choice
 
def main():
    global flip_time
    flip_time = int(input("How many times to flip the coin? "))
    coin_flipper(flip_time)

# prints return of each flip n times
def coin_flipper(n):
    coin = ["heads", "tails"]

    heads_count = 0
    tails_count = 0

    for i in range(n):
        result = choice(coin)
        print(result)
    
        if result == "heads":
         heads_count += 1 
        elif result == "tails":
         tails_count += 1 
    
    print("\n***results***:")
    print(f"\nTotal flips: {flip_time}")
    print(f"\nHeads: {heads_count}")
    print(f"tails: {tails_count}")

main()