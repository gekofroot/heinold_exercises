# Chapter 5
# 5.9 Exercises
# 13.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def multiplication_game():
    n(1)

    correct_answers = 0
    incorrect_answers = 0
    games = 5

    for number in range(0, games):

        number_a = randint(1, 10)

        number_b = randint(1, 10)

        solution = number_a * number_b

        print(number_a, "x", number_b)
        n()

        input_answer = eval(input("asnwer: "))

        if input_answer == solution:
            print(input_answer, "is correct")
            print(f"correct answer is, {solution}")
            correct_answers += 1
            n()
        else:
            print(input_answer, "is incorrect")
            print(f"correct answer is {solution}")
            incorrect_answers += 1
            n()

    print("correct answers:", correct_answers)
    print("incorrect answers:", incorrect_answers)

    n()
    if correct_answers == 5:
        print("good job")
    elif 4 >= correct_answers > 3:
        print("alright")
    elif 3 >= correct_answers >= 2:
        print("okay")
    elif 2 > correct_answers == 0:
        print("needs work")

    n(2)


multiplication_game()
