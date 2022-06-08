# Chapter 6
# 6.11 Exercises
# 21.

from random import choice, choices, shuffle


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sen = input("please enter a word: ")

    sen_shuff = []

    sen_shuffd = []

    for x in sen:
        sen_shuff.append(x)

    for x in range(0, len(sen_shuff)):
        for x in choice(sen_shuff):
            sen_shuffd.append(x)
            sen_shuff.remove(x)

    sen_shuffd_s = ""
    for x in sen_shuffd:
        sen_shuffd_s += x

    n()
    print("sen rearanged:", sen_shuffd_s)

    n(2)


name()
