# Chapter 9
# 9.6 Exercises
# 12.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    lis = [randint(0, 1) for i in range(7)]
    print(lis)

    n(2)


name()
