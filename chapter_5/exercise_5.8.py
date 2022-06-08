# Chapter 5
# 5.9 Exercises
# 8.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def swap_value():
    n(1)

    value_x = 1
    value_y = 2
    value_z = 3

    print(value_x)
    print(value_y)
    print(value_z)

    x_temp = value_x
    y_temp = value_y
    z_temp = value_z

    value_x = y_temp
    value_y = z_temp
    value_z = x_temp

    n()
    print(value_x)
    print(value_y)
    print(value_z)

    n(2)


swap_value()
