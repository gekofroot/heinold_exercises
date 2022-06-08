# Chapter 8
# 8.7 Exercises
# 23.

from random import choice, shuffle


def n(x=0):
    print("\n" * x)


def t(x=0):
    t = "\t" * x
    return t


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    assorted_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-={}[]:\"<>;',.?/"

    assorted_items = []
    memory_items = []
    check_against = []

    ungroup_memory_items = []
    regroup_memory_items = []

    # fill list with an assortment of items and shuffle
    for character in assorted_characters:
        assorted_items.append(character)

    # create grouped list of pairs
    for number in range(6):
        group_paired_items = []
        for number in range(3):
            choice_item = choice(assorted_items)

            # sift through repeated items
            if choice_item in check_against:
                while choice_item in check_against:
                    choice_item = choice(assorted_items)
            group_paired_items.append(choice_item)
            group_paired_items.append(choice_item)

            # add items in current group to check list
            for item in group_paired_items:
                check_against.append(item)

        memory_items.append(group_paired_items)

    # ungroup list and shuffle out pairs
    for group in memory_items:
        for item in group:
            ungroup_memory_items.append(item)
    shuffle(ungroup_memory_items)

    # regroup shuffled list
    while len(ungroup_memory_items) > 0:
        regroup_memory_items.append(ungroup_memory_items[:6])
        ungroup_memory_items = ungroup_memory_items[6:]

    n()
    for row in range(6):
        for column in range(6):
            print(f"{regroup_memory_items[row][column]}", end="   ")
        print(f"\n")

    n(3)


name()
