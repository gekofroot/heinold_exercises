
# Chapter 8
# 8.7 Exercises
# 17b.

from random import randint, choice


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    g_lis = [[34, 23, 12, 42], [54, 1, 43, 53], [7, 29, 67, 4], [83, 6, 2, 28]]
    print(g_lis)

    y_coun = []
    y_len = 0
    y_coun = sum([sum(x) for x in g_lis for y in x]) / len(g_lis)
    y_len = sum([1 for x in g_lis for y in x])

    n()
    print("y coun:", y_coun)
    print("y len:", y_len)
    print("g_lis average:", y_coun / y_len)

    n(2)


name()
