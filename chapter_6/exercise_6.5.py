# Chapter 6
# 6.11 Exercises
# 5.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    new_string = ""

    sen = input("please enter a string: ")

    for x in sen:
        new_string += x
        print(new_string)

    replace_from = new_string[1]

    new_string = new_string.replace(replace_from, "*")

    print(new_string)

    new_string = new_string + "!!!"

    print(new_string)

    n(2)


name()
