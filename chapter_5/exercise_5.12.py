# Chapter 5
# 5.9 Exercises
# 12.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def guess_number():
    n(1)

    score = 0

    for x in range(0, 5):

        random_number = randint(1, 10)

        input_number = randint(1, 10)

        if input_number == random_number:
            print("correct")
            print(f"guess {input_number} answer {random_number}")
            score += 10
            n()
        else:
            print("incorrect")
            print(f"guess {input_number} answer {random_number}")
            if score > 0:
                score -= 1
            n()

    print("final score", score)

    n(2)


guess_number()
