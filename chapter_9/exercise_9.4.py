# Chapter 9
# 9.6 Exercises
# 4.

from os import system


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    unlck = 0
    psword = "this is a password"

    sen = ""
    attempts = 0
    while attempts < 5:
        sen = input("please enter password: ")
        if sen == psword:
            unlck += 1
            system("clear")
            n(4)
            print("\nlogin accepted")
            n(2)
            print("\thome page:\n")
            print("\t", " -" * 10)
            print("\t|", "  " * 9, "|")
            print("\t|", "  " * 9, "|")
            print("\t|", "  " * 9, "|")
            print("\t|", "  " * 9, "|")
            print("\t|", "  " * 9, "|")
            print("\t", " -" * 10)
            system("top")
            n(2)
            break
        else:
            print("invalid entry, please try again")
            attempts += 1

    n()

    if unlck == 0:
        print(
            "please talk to your administrator or visit our help page for further assistance."
        )

    n(2)


name()
