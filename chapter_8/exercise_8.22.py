# Chapter 8
# 8.7 Exercises
# 222.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    lis_a = [1 for i in range(5)]
    lis_b = [0 for i in range(5)]
    map_lis = [[lis_a[i], lis_b[i]] * 3 for i in range(5)]

    n()
    for a in range(5):
        for b in range(5):
            print(map_lis[a][b], end="")
        print()

    n()
    row = eval(input("please enter a row: "))
    column = eval(input("please enter a column: "))

    n()
    picked_row = map_lis[row - 1]
    picked_column = picked_row[column - 1]

    if picked_column == 1:
        print("hit")
    else:
        print("miss")

    n(2)


name()
# Chapter 8
# 8.7 Exercises
# 22.
