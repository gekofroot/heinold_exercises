# Chapter 8
# 8.7 Exercises
# 15.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    num_s = []
    for x in range(6):
        num_s.append(1)
        for y in range(x):
            num_s.append(0)
    print(num_s)

    n()
    num = [y + 1 for y in range(7) for y in range(y)]
    print(num)

    n(2)


name()
