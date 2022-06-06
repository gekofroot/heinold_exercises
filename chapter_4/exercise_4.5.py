# Chapter 4
# 4.5 Exercises
# 5.

import random


def guess_number():
    
    random_number = random.randint(0, 10)
    input_number = int(input("Please guess a number between 1 and 10: "))
    if 100 > input_number > 0:
        if input_number == random_number:
            print(
                "congratulations, the random number was,",
                random_number,
                "and you guessed,",
                input_number,
            )
        else:
            print(
                "Sorry, the random number was,",
                random_number,
                "and you guessed,",
                input_number,
                "your guess was incorrect.",
            )
    else:
        print("Please select a number between 1 and 10...")
        guess_number()

guess_number()
