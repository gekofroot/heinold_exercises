# Chapter 7
# 7.7 Exercises
# 3.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    num = [8, 9, 10]

    num[1] = 17
    print("plus 17:", num)

    num = num + [4, 5, 6]
    print("plus list:", num)

    num.remove(num[0])
    del num[0]
    print("removing first element:", num)

    num.sort()
    print("num sorted:", num)

    num = num * 2
    print("num x 2:", num)

    num[3] = 25
    print("25 at index 3:", num)

    n(2)


name()
