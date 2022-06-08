# Chapter 8
# 8.7 Exercises
# 7.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    win_p = 0
    loss_p = 0

    usnum = [randint(0, 10) for i in range(0, 6)]

    for x in range(1000000):
        ranum = [randint(0, 10) for i in range(0, 6)]
        counter = 0
        count = 0
        for x in ranum:
            if ranum[count] == usnum[count]:
                counter += 1
            count += 1
        if counter == 6:
            win_p += 1
        else:
            loss_p += 1
    print("wins:", win_p)
    print("losses:", loss_p)

    n(2)


name()
