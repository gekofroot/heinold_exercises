# Chapter 9
# 9.6 Exercises
# 15b.

from random import choice
from os import system
from time import sleep


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def t(x=6):
    t = "\t" * x
    return t


def name():

    country_names = [
        "Canada",
        "Egypt",
        "Australia",
        "Morocco",
        "China",
        "Wales",
        "Venezuela",
        "South Africa",
        "India",
        "Moldova",
        "Scotland",
        "Chile",
        "Ireland",
        "Togo",
        "Zambia",
        "Croatia",
        "Poland",
        "Israel",
        "Iran",
        "Fiji",
        "Mexico",
        "Belgium",
        "France",
        "Germany",
        "Italy",
        "USA",
        "Switzerland",
        "Russia",
        "Japan",
        "Spain",
        "England",
        "Brazil",
        "Hong Kong",
        "Denmark",
    ]

    country_name = choice(country_names)

    correct_guess = ""
    correct_guess_increment = ""
    incorrect_guess = ""
    increment_guess = 0
    sleep_time = 4

    correct_guess_list = []
    for x in range(len(country_name)):
        correct_guess_list += "-"

    for x in correct_guess_list:
        correct_guess += x

    number = 0
    while increment_guess < 5:
        system("clear")
        n(4)
        print(f"{t()}correct guesses: {correct_guess}")
        print(f"{t()}incorrect guesses: {incorrect_guess}")
        n()
        user_guess = input(f"{t()}please guess a letter: ")
        repeat_guess = f"{t(4)}you have already guessed the letter {user_guess}, please select another"
        if user_guess.capitalize() == country_name[0]:
            if user_guess.capitalize() not in correct_guess:
                user_guess = user_guess.capitalize()
        else:
            user_guess.lower()
        if user_guess in country_name:
            if user_guess not in correct_guess_increment:
                correct_guess_increment += user_guess
            if user_guess not in correct_guess:
                count = 0
                for x in country_name:
                    if user_guess == x:
                        correct_guess_list[count] = user_guess
                        number += 1
                    count += 1

                correct_guess = ""
                for x in correct_guess_list:
                    correct_guess += x
                print(f"\n\n{t()}    {user_guess} is correct")
                if number == len(country_name):
                    sleep(2)
                    system("clear")
                    sleep(2)
                    n(10)
                    print(f"{t(8)}word completed")
                    sleep(3)
                    system("clear")
                    break

                sleep(sleep_time)
                system("clear")
            else:
                n(1)
                print(repeat_guess)
                sleep(sleep_time)
                system("clear")

        elif user_guess not in country_name:
            if user_guess.capitalize() not in country_name:
                n(1)
                incorrect_guess += user_guess
                increment_guess += 1
                print(f"{t()}    {user_guess} is incorrect")
                sleep(sleep_time)
                system("clear")
            else:
                n(1)
                print(repeat_guess)
                sleep(sleep_time)
                system("clear")

    guess_total = len(correct_guess_increment) + len(incorrect_guess)
    sleep(3)
    n(10)
    print(f"{t(8)}Country: {country_name}")
    n()
    print(f"{t()}{number} out of the {guess_total} letters you guessed were correct")
    if len(correct_guess_increment) > 0:
        print(f"{t()}your correct guesses were: {correct_guess_increment}")
        if len(incorrect_guess) == 0:
            print(f"\n{t()}you guessed all letters correctly, well done")
        else:
            print(f"{t()}your incorrect guesses were: {incorrect_guess}")
    else:
        print(f"{t()}your incorrect guesses were: {incorrect_guess}")
        print(f"\n{t()}sorry, none of your guesses were correct")

    n(27)


name()
