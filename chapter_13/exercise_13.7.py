# Chapter 3
# 13.6 Exercises
# 7.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    def random_return():
        number = eval(input("please enter number: "))

        digit_list = ""
        random_number = randint(0, 199999)
        digit_list += str(random_number)
        count = 0
        for list_number in digit_list:
            count += 1
        if count != number:
            while count != number and count != 0:
                print(f"the number {random_number} has a length of {count}... ")
                digit_list = ""
                random_number = randint(0, 199999)
                digit_list += str(random_number)
                count = 0
                for list_number in digit_list:
                    count += 1

        print(f"\nthe number {random_number} has a length of {count}")

    random_return()

    n(2)


name()
