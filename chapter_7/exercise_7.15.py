# Chapter 7
# 7.7 Exercises
# 15.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    let = "abcdefghijklmnopqrstuvwxyz"
    sen = "message"
    print(sen)

    sen_m = []
    num_s = []
    for x in sen:
        sen_m.append(x)

    print(sen_m)

    n()
    indx = 1
    for x in sen_m:
        print("x now:", x)
        num_s.append(x)
        print("num_s:", num_s)
        print("num proc")
        for x in num_s:
            if x in let:
                print(x)

    n(2)


name()
