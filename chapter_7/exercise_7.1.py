
# Chapter 7
# 7.7 Exercises
# 1.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    num = eval(input("please enter a list: "))

    n()
    print("total number of items in list:", len(num))

    print("last item in list:", num[-1])

    print("list in reverse order:", num[::-1])

    count = 0
    if 5 in num:
        print("yes, list contains 5")
        count += 1
    else:
        print("list does not contain the number 5.")

    print("list contains the number 5", count, "times")

    num = num[1:-1]

    num.sort()

    print("both first and last items removed, and list sorted:", num)

    count = 0
    for x in num:
        if x < 5:
            count += 1

    print(count, "integers in list are less than 5")

    n(2)


name()
