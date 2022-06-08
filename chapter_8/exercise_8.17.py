# Chapter 8
# 8.7 Exercises
# 17.

from random import randint, choice


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    lis_a = [0 for i in range(10)]
    print(lis_a)

    lis_b = [i * i for i in range(8)]
    print(lis_b)

    g_lis = [122, 42, 34, 43, 12]
    lis_c = [i * 10 for i in g_lis]
    print(lis_c)

    g_lis = "Concatenation"
    lis_d = [i * 2 for i in g_lis]
    print(lis_d)

    g_lis = ["one", "two", "three", "four", "five", "six"]
    lis_e = [i[0] for i in g_lis]
    print(lis_e)

    g_lis = [122, 42, 34, 43, 12]
    lis_f = [i for i in g_lis if i < 100]
    print(lis_f)

    g_lis = ["one", "two", "three", "four", "five", "six"]
    lis_g = [i[0] for i in g_lis if len(i) == 3]
    print(lis_g)

    n()
    L = []
    for x in range(2):
        for y in range(2):
            L.append([x, y])
    print(L)

    L_b = [[x, y] for x in range(2) for y in range(2)]
    print(L_b)

    L_c = [[x, y] for x in range(4) for y in range(x)]
    print(L_c)

    n()
    lis_e = [randint(0, 100) for i in range(51)]
    print(lis_e)

    g_lis = [122, 42, 34, 43, 12]
    lis_f = [i * 2 for i in g_lis]
    print(lis_f)

    g_lis = [122, 42, 34, 43, 12]
    lis_g = len([i for i in g_lis if i > 50])
    print(lis_g)

    g_lis = [randint(0, i) for i in range(100)]
    lis_h = [g_lis.count(i) for i in g_lis]
    print(lis_h)

    g_lis = "abcdefghijklmnopqrstuvwxyz"
    lis_i = [choice(g_lis) for i in range(1000)]
    # print(lis_i)

    g_lis = [[x, y + x] for x in range(1, 6) if x % 2 == 1]  # if y % 2 == 0]
    lis_j = [[y, x] for x, y in g_lis]
    print(g_lis)
    print(lis_j)

    g_lis = [[0, 1]]
    print(g_lis)
    lis_k = [[x, y] for x, y in g_lis]
    print(lis_k)

    n()
    g_lis = [1, 0]
    lis_l = [x for i in range(10) for y in range(x)]
    print(lis_l)

    n(2)


name()
