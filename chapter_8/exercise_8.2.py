# Chapter 8
# 8.7 Exercises
# 2.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    num = input("please enter five numbers:  ")

    num = "+".join(num)

    print(num)

    n(2)


name()
