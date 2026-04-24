# Create a random number guessing game with python.

import random

print("🎯 Number Guessing Game")

num = random.randint(1, 10)
tries = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    tries += 1

    if guess == num:
        print(f"Correct! You guessed it in {tries} tries.")
        break
    elif guess > num:
        print("Go a little lower.")
    else:
        print("Go a little higher.")
