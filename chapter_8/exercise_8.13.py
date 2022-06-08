# Chapter 8
# 8.7 Exercises
# 13.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    l_lis = [
        "I",
        "walked",
        "to",
        "the",
        "grocery",
        "store",
        "to",
        "buy",
        "some",
        "lettuce",
    ]

    lis_a = [i[1:] for i in l_lis]
    print(lis_a)

    lis_b = [len(i) for i in l_lis]
    print(lis_b)

    lis_c = [i for i in l_lis if len(i) > 3]
    print(lis_c)

    n(2)


name()
