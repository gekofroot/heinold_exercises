# Chapter 8
# 8.7 Exercises
# 20.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    randlis = [
        [randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)]
        for x in range(4)
    ]

    rowa = []
    rowa_2 = []

    chckag = 0
    count = 0
    count_2 = 3
    for x in randlis:
        rowa.append(x[count])
        count += 1
        rowa_2.append(x[count_2])
        count_2 -= 1
        if sum(x) == sum(randlis[0]):
            chckag += 1
    if sum(rowa) == sum(randlis[0]):
        chckag += 1
    if sum(rowa_2) == sum(randlis[0]):
        chckag += 1

    if chckag == 6:
        print("list", randlis, "is a magic square.")
    else:
        print("list", randlis, "is not a magic square.")
    n(2)


name()
