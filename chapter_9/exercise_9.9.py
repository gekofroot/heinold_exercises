# Chapter 9
# 9.6 Exercises
# 9.

from math import fabs
import time


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    init_guess = eval(input("please enter an initial value: "))

    count = 0
    cns = 1
    res = 0
    while count <= 10:
        res = (init_guess + 5 / init_guess) / 2
        print("res is:", res)
        init_guess = res
        print("init guess is:", init_guess)
        time.sleep(1)
        count += 1
        n()

    n(2)


name()
