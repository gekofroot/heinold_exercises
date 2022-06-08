# Chapter 9
# 9.6 Exercises
# 10.

from random import choice


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    w_lis = [
        "onee",
        "two",
        "thhree",
        "fouur",
        "five",
        "six",
        "sevenn",
        "eight",
        "niinne",
        "ten",
    ]

    doblet = []
    non_doblet = []

    count = 0
    while count < len(w_lis):
        for word in w_lis:
            for let in word:
                if word.count(let) > 1:
                    doblet.append(word)
            count += 1

    for x in w_lis:
        if x not in doblet:
            non_doblet.append(x)

    print(choice(non_doblet))

    n(2)


name()
