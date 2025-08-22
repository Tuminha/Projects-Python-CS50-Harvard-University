"""
Implement a program that:
1. Prompts the user for a level, n.
2. If the user does not input a positive integer, the program should prompt again.
3. Randomly generates an integer between 1 and n, inclusive, using the random module.
4. Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
5. If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
6. If the guess is larger than that integer, the program should output Too large! and prompt the user again.
7. If the guess is the same as that integer, the program should output Just right! and exit.
"""

import random
import sys

def main():
    # Get the level from the user
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            pass

    # Generate a random number between 1 and the level
    secret_number = random.randint(1, level)

    # Start the guessing game
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue

            if guess < secret_number:
                print("Too small!")
            elif guess > secret_number:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit(0)
        except ValueError:
            pass

if __name__ == "__main__":
    main()
