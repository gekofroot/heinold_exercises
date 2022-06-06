# Chapter 4
# 4.5 Exercises
# 10.

import random
from os import system
from time import sleep


def n(x=0):
    print("\n" * x)


def t(x=0):
    t = "\t" * x
    return t


def multiplication_game():

    global correct
    global incorrect

    correct = 0
    incorrect = 0
    sleep_time = 3
    tab_space = 6

    system("clear")

    def start_game():
        n(6)

        def add_correct():
            global correct
            correct += 1

        def add_incorrect():
            global incorrect
            incorrect += 1

        number_of_games = eval(
            input(
                f"{t(tab_space)}how many rounds would you like to play? \n\n{t(tab_space)} >>>  "
            )
        )

        question_number = 1
        system("clear")
        for x in range(number_of_games):
            n(6)

            print(f"{t(tab_space)}round {question_number} / {number_of_games}\n")

            random_number_a = random.randint(1, 10)
            random_number_b = random.randint(1, 10)
            answer = random_number_a * random_number_b

            guess_answer = input(
                f"{t(tab_space)}press 'q' to quit\n\n{t(tab_space)}question number {question_number}: {random_number_a} x {random_number_b} = "
            )
            if guess_answer == "q":
                system("clear")
                n(6)
                print(f"{t(tab_space)}exiting on question {question_number}")
                break
            elif int(guess_answer) == answer:
                n()
                print(f"{t(tab_space)}correct")
                add_correct()
            elif (guess_answer) != answer:
                n()
                print(f"{t(tab_space)}incorrect, the answer is {answer}")
                add_incorrect()

            question_number += 1

            sleep(sleep_time)
            system("clear")

        n(6)
        print(f"{t(tab_space)}correct answers: {correct}")
        print(f"{t(tab_space)}incorrect answers: {incorrect}")

    start_game()
    n(6)

multiplication_game()
