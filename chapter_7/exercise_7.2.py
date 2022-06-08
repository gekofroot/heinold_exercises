# Chapter 7
# 7.7 Exercises
# 2.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    num = []

    for x in range(20):
        num.append(randint(0, 100))

    print("num:", num)

    av = sum(num) / len(num)

    print("average:", av)

    num.sort()
    print("num sorted:", num)

    print("largest number:", num[-1])

    print("smallest number:", num[0])

    print("second largest number:", num[-2])

    print("second smallest number:", num[1])

    count = 0
    for x in num:
        if x % 2 == 0:
            count += 1

    print("there are", count, "even numbers in list")

    n(2)


name()
# Chapter 7
# 6.11 Exercises
# 1.
