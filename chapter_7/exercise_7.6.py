# Chapter 7
# 7.7 Exercises
# 6.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    list_a = []
    for x in range(50):
        list_a.append(x)

    list_b = []
    for x in range(50):
        x = x ** 2
        list_b.append(x)

    list_c = []
    let = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    count_2 = 1
    for x in range(len(let)):
        list_c.append(let[count] * count_2)
        count += 1
        count_2 += 1

    print("list_a:", list_a)
    n()
    print("list_b:", list_b)
    n()
    print("list_c:", list_c)

    n(2)


name()
