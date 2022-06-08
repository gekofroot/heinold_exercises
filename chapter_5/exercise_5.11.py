# Chapter 5
# 5.9 Exercises
# 11.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def number_factorial():
    n(1)

    integers = []

    input_number = randint(1, 10)
    print(f"number is: {input_number}")
    n()

    for x in range(1, input_number + 1):
        integers.append(x)

    print(f"integers between 1 and {input_number} {integers}")

    total = input_number / input_number
    print(f"total:, {total}")
    n()

    for x in range(1, input_number + 1):
        total *= x
        print(total)
    n()

    if input_number > 0:
        print(f"factoral of {input_number} is {int(total)}")
    else:
        print(f"factorial of 0 is 0")

    n(2)


number_factorial()
