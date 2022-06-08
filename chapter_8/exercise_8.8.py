# Chapter 8
# 8.7 Exercises
# 8.

from random import choice


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sen = input("please enter names: ")
    num = eval(input("please enter number of draws: "))

    names = sen.split()

    draw = []

    for x in range(num):
        draw += names

    print("selected name is:", choice(draw))

    n(2)


name()
