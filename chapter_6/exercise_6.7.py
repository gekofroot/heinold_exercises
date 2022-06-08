# Chapter 6
# 6.11 Exercises
# 7.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sen = input("please enter a word: ")

    sen_reverse = ""

    for x in range(0, 1):
        while x <= len(sen) - 1:
            sen_reverse += sen[-x - 1]
            x += 1

    n()
    if sen == sen_reverse:
        print(sen, "backwards is:", sen_reverse)
        print(sen, "is a palindrome")
    else:
        print(sen, "backwards is", sen_reverse)
        print(sen, "is not a palindrome")

    n(2)


name()
