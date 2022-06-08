# Chapter 8
# 8.7 Exercises
# 14.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    i = [str(i).split() for i in range(100, 1000) if str(i)[0] == str(i)[-1]]
    print(i)

    n(2)


name()
