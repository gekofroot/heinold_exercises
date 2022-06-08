# Chapter 3
# 13.6 Exercises
# 10.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    lenum = [randint(0, 100) for y in range(10)]

    chose_number = eval(input(f"please select a number between {0, 100}: "))

    def closest(number_list, number):

        number_list.sort()
        print(f"\nnumber list: {number_list}")
        less_than_num = []
        for num in number_list:
            if number > num:
                less_than_num.append(num)

        less_than_num.sort()
        if len(less_than_num) == 0:
            print(f"\nthe are no elements in number list less than {number}")
        else:
            print(
                f"\nthe largest element in number list less than {number} is {less_than_num[-1]}"
            )

    closest(lenum, chose_number)

    n(2)


name()
# Chapter 3
# 13.6 Exercises
# 1.
