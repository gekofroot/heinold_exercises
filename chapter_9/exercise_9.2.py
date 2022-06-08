# Chapter 9
# 9.6 Exercises
# 2.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    x = 0
    sen = input("please enter sentence: ")
    while x < len(sen):
        if x % 2 == 1:
            print(sen[x])
        x += 1

    n(2)


name()
