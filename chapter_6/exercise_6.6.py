# Chapter 6
# 6.11 Exercises
# 6.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    s = input("please enter a string: ")

    s = s.lower()

    for x in s:
        if x in ".,":
            s = s.replace(x, " ")

    print(s)

    n(2)


name()
