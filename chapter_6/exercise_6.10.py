# Chapter 6
# 6.11 Exercises
# 10.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sen = input("please enter a string: ")
    n()

    sen = sen.upper()
    for x in sen:
        x = x * 2
        print(x, "\n")

    n(2)


name()
