# Chapter 8
# 8.7 Exercises
# 18.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    randlis = [
        [
            randint(0, 100),
            randint(0, 100),
            randint(0, 100),
            randint(0, 100),
            randint(0, 100),
            randint(0, 100),
            randint(0, 100),
            randint(0, 100),
            randint(0, 100),
            randint(0, 100),
        ]
        for i in range(10)
    ]
    print(randlis)

    n()
    row_c = randlis[2]
    row_c.sort()
    print("largest value in third row:", row_c[-1])

    column_six = []
    for x in randlis:
        count = 0
        for y in x:
            if count == 6:
                column_six.append(y)
            count += 1

    n()
    column_six.sort()
    print("smallest value in column six:", column_six[0])

    n(2)


name()
