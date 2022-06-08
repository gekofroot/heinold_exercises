# Chapter 11
# 11.5 Exercises
# 7.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    numbers = [[randint(0, 10) for x in range(5)] for y in range(5)]
    print(f"{numbers}\n")

    flattened_numbers = [y for x in numbers for y in x]
    print(f"{flattened_numbers}\n")

    key_val = {}
    for number in flattened_numbers:
        key_val[number] = flattened_numbers.count(number)

    index = 0
    for x, y in key_val.items():
        print(f"{x}: {y}")

    n()
    index = 0
    most_common = 0
    second_most_common = 0
    third_most_common = 0

    for x, y in key_val.items():
        if y > index:
            index = y
            print(f"{x}: {y}")

    n(2)


name()
