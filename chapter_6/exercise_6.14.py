# Chapter 6
# 6.11 Exercises
# 14.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sen_f = input("please enter your first name in lowercase: ")
    sen_m = input("please enter your middle name in lowercase: ")
    sen_l = input("please enter your last name in lowercase: ")

    name = [sen_f, sen_m, sen_l]

    space = []
    firstname = []
    middlename = []
    lastname = []

    count = 0

    n()
    for x in name:
        x = x.capitalize()
        print(x, end=" ")

    n(2)


name()
