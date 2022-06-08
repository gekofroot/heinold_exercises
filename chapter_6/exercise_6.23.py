# Chapter 6
# 6.11 Exercises
# 23.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    # sen = input("please enter a string: ")
    sen = "secret message"

    print(sen)

    sen_n = ""

    n()
    sen_g1 = sen[::3]
    print(sen_g1)
    sen_g2 = sen[1::3]
    print(sen_g2)
    sen_g3 = sen[2::3]
    print(sen_g3)

    sen_n += sen_g1
    sen_n += sen_g2
    sen_n += sen_g3

    n()
    print(sen_n)

    n(2)


name()
