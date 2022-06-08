# Chapter 6
# 6.11 Exercises
# 9.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)
    dlm(70)
    n(1)

    num = input("please enter a number: ")
    n()

    space = ""
    space_count = 0
    count = 0
    while count < len(num) - 1:
        for x in num:
            print(space, x)
            count += 1
            space = space + " "

    n(2)


name()
