# Chapter 7
# 7.7 Exercises
# 14.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    # 10 cm = 1 inch
    # 12 inches = 1 foot
    # 3 feet = 1 yard
    # 10 yards = 1 mile

    conv_un = ["cm", "inches", "yards", "miles"]
    sel = []

    count = 1
    for x in conv_un:
        sel.append(count)
        count += 1
    print(conv_un)
    print(sel)

    n()
    num = eval(input("please enter length in feet: "))
    sen = eval(
        input("please enter conversion unit  0. cm  1. inches  2. yards  3. miles  : ")
    )

    n()

    for x in range(len(sel)):
        print(x)
        if x == sen:
            print("converting ", num, " feet to ", conv_un[x], sep="")
            # print(num / 120)
            break
    else:
        print("invalid entry, please enter an available option")

    n(2)


name()
