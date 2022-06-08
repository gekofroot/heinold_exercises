# Chapter 6
# 6.11 Exercises
# 8.

from random import randint, choice


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)
    dlm(70)

    num = eval(input("how many email addresses will be entered? "))

    n()
    print("email addresses entered:", num)

    email_addresses = []

    add_list = ["@student.college.edu", "@prof.college.edu"]

    n()
    count = 0
    for x in range(1, num + 1):
        count += 1
        # sen = input("please enter email addresses: ")
        sen = choice(add_list)
        email_addresses.append(sen)

    stud = "@student.college.edu"
    prof = "@prof.college.edu"

    stud = "\@student.college.edu"
    prof = "\@prof.college.edu"

    stud_address = 0
    prof_address = 0

    n()
    for x in email_addresses:
        if x in stud:

            stud_address += 1
        elif x in prof:
            prof_address += 1

    print("number of student addresses", stud_address)
    print("number of proffessor addresses", prof_address)

    n()
    if prof_address > 0:
        print("proffessor address have been entered")
    elif stud_address > 0:
        print("all addresses are student addresses")
    else:
        print("no address have been added")

    n(2)


name()
