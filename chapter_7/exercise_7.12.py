# Chapter 7
# 7.7 Exercises
# 12.

from random import *


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    num = []

    for x in range(101):
        num.append(randint(0, 1))

    count = 0
    hstrn = 0
    indx = 0
    count_2 = 0
    hstrn_2 = 0
    indx_2 = 0
    print(num)
    for x in num:
        if x == 0:
            count += 1
            indx += 1
        else:
            if indx > hstrn:
                hstrn = indx
            indx = 0
        if x == 1:
            count_2 += 1
            indx_2 += 1
        else:
            if indx_2 > hstrn_2:
                hstrn_2 = indx_2
            indx_2 = 0

    n()
    print("count:", count)
    print("hstindx:", hstrn)
    print("indx:", indx)

    n()
    print("count_2:", count_2)
    print("hstindx_2:", hstrn_2)
    print("indx_2:", indx)

    n(2)


name()
# Chapter 7
# 7.7 Exercises
# 1.
