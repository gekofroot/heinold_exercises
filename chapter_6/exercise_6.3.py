# Chapter 6
# 6.11 Exercises
# 3.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    opening_parentheses = 0

    closing_parentheses = 0

    enform = input("please enter a formula: ")

    for x in enform:
        if x in "(":
            opening_parentheses += 1
        elif x in ")":
            closing_parentheses += 1

    if opening_parentheses > closing_parentheses:
        print("missing one or more closing parentheses.")
    elif opening_parentheses < closing_parentheses:
        print("missing one or more opening parentheses.")

    n(2)


name()
