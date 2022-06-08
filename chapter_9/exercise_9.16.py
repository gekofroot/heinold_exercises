# Chapter 9
# 9.6 Exercises
# 16.

from random import choice, shuffle


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    assorted_items = []
    grid_group = []
    check_against = []

    ungroup_grid = []
    regroup_grid = []

    assorted_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=[]\;',./_+{}|:\"<>?"

    # fill assorted_items with characters
    for character in assorted_characters:
        assorted_items.append(character)

    # created grouped list of pairs
    for number in range(6):
        group_paired_items = []
        for number in range(3):
            choice_item = choice(assorted_items)

            # sift through repeate items
            if choice_item in check_against:
                while choice_item in check_against:
                    choice_item = choice(assorted_items)
            group_paired_items.append(choice_item)
            group_paired_items.append(choice_item)

            # add items in current group to check against
            for item in group_paired_items:
                check_against.append(item)

        grid_group.append(group_paired_items)

    # ungroupd grid and shuffle
    for group in grid_group:
        for item in group:
            ungroup_grid.append(item)
    shuffle(ungroup_grid)

    # create asterisk grid
    count = 0
    for number in range(6):
        group_paired_items = []
        for number in range(3):
            choice_item = "*"

            group_paired_items.append(choice_item)
            group_paired_items.append(choice_item)

        grid_group[count] = group_paired_items
        count += 1

    print(" ")

    print(grid_group)
    n(2)
    for row in range(6):
        for column in range(6):
            print(grid_group[row][column], end="  ")
        print("\n")

    # regroup grid
    while len(ungroup_grid) > 0:
        regroup_grid.append(ungroup_grid[:6])
        ungroup_grid = ungroup_grid[6:]

    n(2)
    for row in range(6):
        for column in range(6):
            print(regroup_grid[row][column], end="  ")
        print("\n")

    # enter coordinates
    coord_a_1 = eval(input("please enter row: "))
    coord_a_2 = eval(input("please enter column: "))

    n()
    coord_b_1 = eval(input("please enter row: "))
    coord_b_2 = eval(input("please enter column: "))

    # n(2)
    # for row in range(6):
    #    for column in range(6):
    #        print(regroup_grid[row][column], end = '  ')
    #    print('\n')

    n(2)


name()
