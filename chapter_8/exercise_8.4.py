# Chapter 8
# 8.7 Exercises
# 4.

from random import shuffle
from string import punctuation


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sen = input("please enter a sentence: ")
    for c in punctuation:
        sen = sen.replace(c, "")
    sen = sen.split()
    shuffle(sen)

    sen[0] = sen[0].capitalize()
    sen = " ".join(sen)

    sen += "."
    sens = ""
    for x in sen:
        sens += x
    print(sens)

    n(2)


name()
