# Chapter 3
# 13.6 Exercises
# 1.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    def rectangle(m, n):

        horizontal = "*" * n
        for x in range(m):
            print(horizontal)

    rectangle(4, 10)

    n(2)


name()
