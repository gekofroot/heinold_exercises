# Chapter 6
# 6.11 Exercises
# 19.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    # num = input("please enter a number: ")
    # num = "1000000"
    # num = "100000"
    # num = "10000"
    num = "1000"

    num_f = []

    for x in num:
        num_f.append(x)

    count = 0
    num_f.append(num_f[count])
    num_f.remove(num_f[count])
    print(num_f)

    num_f_join = ""

    for x in num_f:
        num_f_join += x
    n()
    print("num f join is:", num_f_join)

    n()
    count = 1
    for x in num_f:
        print(count, x)
        count += 1
        if count % 4 == 0:
            print("mult:", count)
            num_f.insert(count - 4, ",")
            num_f_join += ","
            print("num f loop:", num_f)
            print("num f join loop:", num_f_join)
    n()
    print(num_f)

    count = 0
    for x in range(0, len(num_f) - 1):
        num_f.append(num_f[count])
        num_f.remove(num_f[count])
    print(num_f)

    num_f_join = ""

    for x in num_f:
        num_f_join += x
    n()
    print("num f join is:", num_f_join)

    n(2)


name()
