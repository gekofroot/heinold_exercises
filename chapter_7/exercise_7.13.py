# Chapter 7
# 7.7 Exercises
# 13.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    num = []
    for x in range(20):
        num.append(randint(0, 10))
    print(num)
    chk_num = []

    for x in num:
        if x not in chk_num:
            chk_num.append(x)
    n()
    print(chk_num)

    n(2)


name()
