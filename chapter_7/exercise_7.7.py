# Chapter 7
# 7.7 Exercises
# 7.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    # num = [13, 32, 213, 52, 32]
    # num_2 = [112, 2, 23, 24, 26]
    num = eval(input("please enter list 1: "))
    num_l = []
    for x in num:
        num_l.append(x)

    num_2 = eval(input("please enter list 2 with same size as list 1: "))
    num_l_2 = []
    for x in num_2:
        num_l_2.append(x)

    if len(num_l) != len(num_l_2):
        print("invalid entry, lists are of different lengths")
    else:
        num_3 = []
        for x in range(len(num_l)):
            n_ad = num_l[x] + num_l_2[x]
            num_3.append(n_ad)
        print(num_3)

    n(2)


name()
