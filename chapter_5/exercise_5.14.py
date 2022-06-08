# Chapter 5
# 5.9 Exercises
# 14.

from random import randint, shuffle, choice


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def monty_hall(number_of_doors):
    n(1)

    win = 0
    loss = 0
    games_played = 0

    picked_door = []

    input_number = eval(input(f"how many iterations? "))

    for x in range(0, input_number):

        items = ["prize", "goat", "goat"]

        door_a = choice(items)
        items.remove(door_a)

        door_b = choice(items)
        items.remove(door_b)

        door_c = choice(items)
        items.remove(door_c)

        shuffled_items = [door_a, door_b, door_c]

        # pickdoor = eval(input(f'please pick a door  1. door a  2. door b  3. door c  door d: '))
        pickdoor = randint(1, 4)

        if pickdoor == 1:
            picked_door = door_a
            shuffled_items.remove(door_a)
        elif pickdoor == 2:
            picked_door = door_b
            shuffled_items.remove(door_b)
        elif pickdoor == 3:
            picked_door = door_c
            shuffled_items.remove(door_c)
        elif pickdoor == 4:
            picked_door = door_c
            shuffled_items.remove(door_c)

        for x in shuffled_items:
            if x == "goat":
                shuffled_items.remove(x)

        # keep_door = eval(input(f'change doors?  1. keep door  2. change door: '))
        keep_door = randint(1, number_of_doors)

        if keep_door == 1:
            pass
        elif keep_door == 2:
            picked_door = shuffled_items[0]

        if picked_door == "prize":
            win += 1
        else:
            loss += 1
        games_played += 1
    percentage = (win / games_played) * 100
    print(percentage)

    n(2)


monty_hall(number_of_doors)
