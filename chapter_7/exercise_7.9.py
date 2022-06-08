# Chapter 7
# 7.7 Exercises
# 9.

from random import randint, choice


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    ten = 0
    eleven = 0
    twelve = 0

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    num_times = 10
    count = 0
    for x in range(num_times):
        d_1 = choice(nums)
        d_2 = choice(nums)
        # print(count, "d_1:", d_1)
        # print(count, "d_2:", d_2)
        # n()
        count += 1

        if d_1 == 1:
            one += 1
        elif d_1 == 2:
            two += 1
        elif d_1 == 3:
            three += 1
        elif d_1 == 4:
            four += 1
        elif d_1 == 5:
            five += 1
        elif d_1 == 6:
            six += 1
        elif d_1 == 7:
            seven += 1
        elif d_1 == 8:
            eight += 1
        elif d_1 == 9:
            nine += 1
        elif d_1 == 10:
            ten += 1
        elif d_1 == 11:
            eleven += 1
        elif d_1 == 12:
            twelve += 1

        if d_2 == 1:
            one += 1
        elif d_2 == 2:
            two += 1
        elif d_2 == 3:
            three += 1
        elif d_2 == 4:
            four += 1
        elif d_2 == 5:
            five += 1
        elif d_2 == 6:
            six += 1
        elif d_2 == 7:
            seven += 1
        elif d_2 == 8:
            eight += 1
        elif d_2 == 9:
            nine += 1
        elif d_2 == 10:
            ten += 1
        elif d_2 == 11:
            eleven += 1
        elif d_2 == 12:
            twelve += 1

    n()
    print(f"rolling one: {one / num_times * 100:.3f}")
    print(f"rolling two: {two / num_times * 100:.3f}")

    print(f"rolling three: {three / num_times * 100:.3f}")
    print(f"rolling four: {four / num_times * 100:.3f}")

    print(f"rolling five: {five / num_times * 100:.3f}")
    print(f"rolling six: {six / num_times * 100:.3f}")

    print(f"rolling seven: {seven / num_times * 100:.3f}")
    print(f"rolling eight: {eight / num_times * 100:.3f}")

    print(f"rolling nine: {nine / num_times * 100:.3f}")
    print(f"rolling ten: {ten / num_times * 100:.3f}")

    print(f"rolling eleven: {eleven / num_times * 100:.3f}")
    print(f"rolling twelve: {twelve / num_times * 100:.3f}")

    n(2)


name()
