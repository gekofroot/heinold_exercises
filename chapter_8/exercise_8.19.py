# Chapter 8
# 8.7 Exercises
# 19.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    ranlis = [x for y in range(4) for x in range(1, 3)]

    ranlis_rev = [x for x in ranlis]
    ranlis_rev.reverse()

    upd_ranlis = [ranlis, ranlis_rev] * 4

    print("upd ranlis:\n")
    for x in range(8):
        for y in range(8):
            print(upd_ranlis[x][y], end="")
        print()

    n(2)


name()
