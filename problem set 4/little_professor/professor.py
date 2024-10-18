"""
implement a program that:

Prompts the user for a level, 
. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. 
If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

import random


def main():
    ...


def get_level():
    ...


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
"""

import random


def main():
    score = 0
    level = get_level()
    number_exercises = 10
    for _ in range(number_exercises): #generate 10 problems. Why using "_" instead of "i"? Beacuse we don't need to use the variable.
        x = generate_integer(level) #generate random number depends on the level
        y = generate_integer(level) #generate random number depends on the level
        problem = f"{x} + {y} = " #format the problem
        correct_answer = x + y #calculate the correct answer    
        for _ in range(3): #allow 3 tries
            try:
                user_answer = int(input(problem)) #prompt the user to solve the problem
                if user_answer == correct_answer:
                    score += 1 #increment the score if the answer is correct
                    break #break the loop if the answer is correct
                else:
                    print("EEE") #print EEE if the answer is incorrect
            except ValueError:
                print("EEE") #print EEE if the answer is not a number
        else:
            print(correct_answer) #print the correct answer if the user has used all the tries
    print(f"Score: {score}") #print the final score


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
