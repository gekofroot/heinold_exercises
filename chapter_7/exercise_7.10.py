# Chapter 7
# 7.7 Exercises
# 10.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    num = [34, 23, 52, 24, 27, 24]
    print(num)

    num.insert(0, num[-1])
    del num[-1]

    print(num)

    n(2)


name()
