# Chapter 8
# 8.7 Exercises
# 24.

from random import randint, choice
from string import punctuation


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    lis_a = [randint(0, 1) for i in range(5)]
    lis_b = [randint(0, 1) for i in range(5)]

    sel_lis = [[lis_a[i], lis_b[i]] * 3 for i in range(5)]
    print("sel_lis:", sel_lis)

    n()
    for a in range(5):
        for b in range(5):
            print(sel_lis[a][b], end=" ")
        print(" \n")

    ran_pic_r = randint(0, 4)
    ran_pic_c = randint(0, 4)

    lis_row = sel_lis[ran_pic_r]
    lis_column = lis_row[ran_pic_c]

    print("lis_row:", lis_row)
    print("lis_column:", lis_column)

    n()
    ne_lis = []
    count = 0
    for x in sel_lis:
        print("x in sel lis", x)
        count_2 = 0
        for y in x:
            print("len x:", len(x))
            print("y is:", y)
            while count_2 < len(x):
                print("count_2:", count_2, "x count", x[count_2])
                if x[count_2] == 1:
                    ne_lis.append([count, count_2])
                count_2 += 1
        count += 1

    n()
    for a in range(5):
        for b in range(6):
            print(sel_lis[a][b], end=" ")
        print(" \n")

    print(ne_lis)

    lis_ch = choice(ne_lis)
    print(choice(ne_lis))

    lis_ch_s = ""
    for x in lis_ch:
        print(x)
        lis_ch_s += str(x)
    for c in punctuation:
        lis_ch_s = lis_ch_s.replace(c, ":")

    lis_ch_s = ":".join(lis_ch_s)
    print(lis_ch_s)

    print(sel_lis[lis_ch_s])

    n(2)


name()
