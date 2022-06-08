# Chapter 8
# 8.7 Exercises
# 21.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    units = ["centimeter", "inch", "foot"]
    print(units)

    num = 12  # eval(input("please enter length: "))

    n()
    conv = eval(input("please enter unit  [0] centimeters [1] inches [2] foot : "))
    n()
    print(num, units[conv])

    n()
    conv_2 = eval(
        input("please enter conversion unit [0] centimeters [1] inches [2] foot : ")
    )
    n()
    print(num, units[conv], "to", units[conv_2])
    n()

    centimeter = 1
    inch = centimeter * 10
    foot = inch * 12
    unit_lis = [[i for i in units]] * 2
    # print(unit_lis)

    n()
    if conv == 0:
        if conv_2 == 0:
            print("no conversion")
        elif conv_2 == 1:
            print("converting", units[conv], "to", units[conv_2])
            calc = num * inch
            print(num, units[conv], "=", calc, units[conv_2])
        elif conv_2 == 2:
            print("converting", units[conv], "to", units[conv_2])
            calc = (num * inch) * foot
            print(num, units[conv], "=", calc, units[conv_2])

    if conv == 1:
        if conv_2 == 0:
            print("converting", units[conv], "to", units[conv_2])
            calc = num * 10
            print(num, units[conv], "=", calc, units[conv_2])
        elif conv_2 == 1:
            print("no conversion")
        elif conv_2 == 2:
            print("converting", units[conv], "to", units[conv_2])
            calc = (num / foot) * 10
            print(num, units[conv], "=", calc, units[conv_2])

    if conv == 2:
        if conv_2 == 0:
            print("converting", units[conv], "to", units[conv_2])
            calc = num / inch
            print(num, units[conv], "=", calc, units[conv_2])
        elif conv_2 == 1:
            print("converting", units[conv], "to", units[conv_2])
            calc = (num / inch) / centimeter
            print(num, units[conv], "=", calc, units[conv_2])
        elif conv_2 == 1:
            print("no conversion")

    n(2)


name()
