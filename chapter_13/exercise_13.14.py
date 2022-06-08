# Chapter 3
# 13.6 Exercises
# 14.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    numbers = [randint(0, 100) for y in range(10)]

    print(f"list: {numbers}\n")

    sort_list = input("sort list? [y, yes] [n, no]: ")
    if sort_list in "y, yes":
        numbers.sort()

    def is_sorted(a_list):
        def sorted_list(sort, sort_list, tof):
            print(f"\n{sort} list: {sort_list}\n\nsorted: {tof}")

        sort_check = []

        count = 0
        unsorted = 0
        for number in a_list:
            sort_check.append(number)
            if number >= sort_check[count]:
                continue
            else:
                unsorted = 1
                break
            count += 1

        if unsorted == 1:
            sorted_list("unsorted", a_list, "False")
        else:
            sorted_list("sorted", a_list, "True")

    is_sorted(numbers)

    n(2)


name()
