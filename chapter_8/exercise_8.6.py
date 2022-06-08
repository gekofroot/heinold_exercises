# Chapter 8
# 8.7 Exercises
# 6.

from random import randint, choice


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    wins = 0
    losses = 0
    for x in range(1000000):

        lotnum = [randint(1, 48) for i in range(0, 6)]
        lotdr = [randint(1, 48) for i in range(0, 6)]

        counter = 0
        count = 0
        for x in lotdr:
            if lotdr[count] == lotnum[count]:
                counter += 1
            count += 1

        if counter == 6:
            wins += 1
        else:
            losses += 1
    print("wins:", wins)
    print("losses:", losses)

    n(2)


name()
