# Chapter 8
# 8.7 Exercises
# 11.

from random import choice


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sen = input("please enter string: ")

    ssen = sen.split()

    angram = []
    for x in ssen:
        y = choice(ssen)
        angram.append(y)

    angram = " ".join(angram)

    print("angram is:", angram)

    n(2)


name()
