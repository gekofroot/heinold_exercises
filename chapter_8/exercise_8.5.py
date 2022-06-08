# Chapter 8
# 8.7 Exercises
# 5.

from random import shuffle, choice


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    list_of_quotes = [
        "the first quote in the list",
        "another quote",
        "the third quote",
        "a quote you may like",
        "the last quote in the list of quotes",
    ]
    shuffle(list_of_quotes)

    print(choice(list_of_quotes))

    n(2)


name()
