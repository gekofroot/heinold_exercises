# Chapter 8
# 8.7 Exercises
# 16.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    nums = [0, 1]

    num_com = [1 for x in range(5) for y in range(x + 1)]

    num = []
    for x in range(5):
        num.append(1)
        for y in range(0 + x):
            num.append(0)

    n()
    print("num:", num)
    print("num_com:", num_com)
    n()
    print("lenof num:", len(num))
    print("lenof num_com:", len(num_com))

    n(2)


name()
