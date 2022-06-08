# Chapter 9
# 9.6 Exercises
# 1.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    i = 0
    while i < 51:
        print(i)
        i += 1

    n(2)


name()
