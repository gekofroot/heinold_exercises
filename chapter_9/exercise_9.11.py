# Chapter 9
# 9.6 Exercises
# 11.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    lis = [[0 for i in range(5)] for y in range(5)]
    print(lis)

    n()
    for x in range(5):
        for y in range(5):
            print(lis[x][y], end="")
        print()

    # print(lis[0][0])

    n()
    count = 0
    while count < 10:
        if lis[randint(0, 4)][randint(0, 4)] == 1:
            print("item is equal to 1")
        else:
            lis[randint(0, 4)][randint(0, 4)] = 1
            count += 1
        n()

    n(2)
    print(lis)

    n()
    for x in range(5):
        for y in range(5):
            print(lis[x][y], end="")
        print()

    n(2)


name()
