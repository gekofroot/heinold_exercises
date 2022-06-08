# Chapter 5
# 5.9 Exercises
# 3.

from math import log


def n(x=0):
    print("\n" * x)


def compute_log():
    n(1)

    input_number = eval(input("please enter a number: "))

    count = 2
    for number in range(count, input_number + 1):
        comp = 1 + (1 / count)
        count += 1

    n()
    solution = comp - log(number)
    print(solution)
    n()


compute_log()
