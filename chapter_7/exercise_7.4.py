# Chapter 7
# 7.7 Exercises
# 4.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    num = eval(input("please enter list containing nunmbers between 1 - 12: "))

    print(num)

    count = 0
    for x in num:
        if x > 10:
            num[count] = 10
            print(x)
        count += 1

    n()
    print(num)

    n(2)


name()
