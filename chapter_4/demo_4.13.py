# Chapter 4
# 4.5 Exercises
# 13.

import os
from random import randint
from time import sleep


def n(x=0):
    print("\n" * x)


def t(x=0):
    t = "\t" * x
    return t


def game():

    sleep_time = 3
    tab_space = 5

    computer_tally = []
    player_tally = []
    tie_tally = []

    def computer_win():
        print(f"{t(tab_space)}computer won \n")
        computer_tally.append(1)

    def player_win():
        print(f"{t(tab_space)}player won \n")
        player_tally.append(1)

    def tie():
        print(f"{t(tab_space)}tie... \n")
        tie_tally.append(1)

    def tally():
        print(f"{t(tab_space)}computer_tally: {sum(computer_tally)}")
        print(f"{t(tab_space)}player_tally: {sum(player_tally)}")
        print(f"{t(tab_space)}tie_tally: {sum(tie_tally)}")
        print(f"{t(tab_space)}\n")

    game = 1

    def match():
        print(f"{t(tab_space)}game: {game}\n")

        computer_choice = randint(1, 3)
        player_choice = int(input(f"{t(tab_space)}  1. rock  2. paper  3. scissors  "))
        print(f"{t(tab_space)}\n")

        print(f"{t(tab_space)}computer choice: computer_choice \n")
        print(f"{t(tab_space)}player choice: {player_choice} \n")
        if player_choice == computer_choice:
            tie()

        elif player_choice == 1 and computer_choice == 2:
            computer_win()

        elif player_choice == 1 and computer_choice == 3:
            player_win()

        elif player_choice == 2 and computer_choice == 1:
            player_win()

        elif player_choice == 2 and computer_choice == 3:
            computer_win()

        elif player_choice == 3 and computer_choice == 1:
            computer_win()

        elif player_choice == 3 and computer_choice == 2:
            player_win()

        else:
            print(f"{t(tab_space)}Please select an available option.")
            match()

    for x in range(0, 5):
        os.system("clear")
        n(6)
        match()
        tally()
        game = game + 1
        sleep(sleep_time)

    if sum(computer_tally) < sum(player_tally):
        os.system("clear")
        n(6)
        tally()
        print(f"{t(tab_space)}player won")

    elif sum(computer_tally) > sum(player_tally):
        os.system("clear")
        n(6)
        tally()
        print(f"{t(tab_space)}computer won")

    else:
        os.system("clear")
        n(6)
        tally()
        print(f"{t(tab_space)}tie game... ")

game()
