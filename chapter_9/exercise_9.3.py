# Chapter 9
# 9.6 Exercises
# 3.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    num = -1
    while num <= 0:
        num = eval(input("please enter a valid weight in kilograms: "))

    pnds = num * 0.25

    print("you weight", pnds, "pounds")

    n(2)


name()
