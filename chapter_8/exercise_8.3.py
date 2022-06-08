# Chapter 8
# 8.7 Exercises
# 3.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sen = input("please enter a sentence: ")
    sen = sen.split()

    count = 0
    for x in sen:
        while count < 1:
            if x not in " ":
                print("third word:", sen[2])
                print("every third word:", sen[2::3])
                count += 1

    n(2)


name()
