# Chapter 11
# 11.5 Exercises
# 5b.

import urllib.request
from pprint import pprint
from html_table_parser.parser import HTMLTableParser
import pandas as pd
from os import system
from time import sleep
from string import punctuation


def name():
    def t(x=5):
        t = "\t" * x
        return t

    def n(x=0):
        print("\n" * x)

    new_current_table = []
    update_standings = input("update standings? ")
    print(update_standings)
    if update_standings == "yes":

        def update_content():
            def url_get_contents(url):
                req = urllib.request.Request(url=url)
                f = urllib.request.urlopen(req)
                return f.read()

            xhtml = url_get_contents(
                "https://www.uefa.com/uefachampionsleague/standings/"
            ).decode("utf-8")

            p = HTMLTableParser()

            p.feed(xhtml)

            current_table = p.tables
            # new_current_table = []

            count = 0
            for item in range(len(current_table)):
                new_current_table.append(current_table[count][:][1:])
                count += 1
                n()

        # update_content()
    else:
        print("cont... ")

    update_standings = input("update stadings? ")
    if update_standings == "yes":
        fln = open("filename", "w")
        fln.write(str(new_current_table))
        fln.close()
    else:
        fln = open("filename", "r")
        flnr = fln.read()
        newer_current_table = ""
        newest_current_table = []
        newer_current_table += flnr
        for c in new_current_table:
            for y in c:
                print("prinum:", y)
                newest_current_table.append(y)

    print("newest current table:", newest_current_table)

    # print("\n\nPandas DATAFRAME\n")
    # print(pd.DataFrame(p.tables[0][1:]))

    teams = []

    team_games_played = []

    team_wins = []

    team_draws = []

    team_losses = []

    goals_for = []

    goals_against = []

    for table_lists in newest_current_table:
        print(table_lists[:][0][:-12])
        teams.append(table_lists[:][0][:-12])
        team_games_played.append(int(table_lists[:][1]))
        team_wins.append(int(table_lists[:][2]))
        team_draws.append(int(table_lists[:][3]))
        team_losses.append(int(table_lists[:][4]))
        goals_for.append(int(table_lists[:][5]))
        goals_against.append(int(table_lists[:][6]))
    n()

    n(1)

    table_stats = {}

    def initialise_screen(num):
        system("clear")
        n(num)

    # while True:
    # team_name = input("team name: ")
    # if team_name == 'q':
    #    break
    # else:
    # wins = eval(input("wins: "))
    # losses = eval(input("losses: "))

    # table_stats[team_name] = [wins, losses]

    count = 0
    while count < len(teams):
        for x in teams, team_wins, team_draws, team_losses:
            table_stats[teams[count]] = [
                team_wins[count],
                team_draws[count],
                team_losses[count],
                goals_for[count],
                goals_against[count],
            ]
        count += 1

    def show_table_stats():

        count = 1
        print(f"{t()}    Table Stats: \n")
        for x, y in table_stats.items():
            print(f"{t()}{count}. {x}: {y[0]} | {y[1]} | {y[2]}\n", end="")
            count += 1

    def show_stat_percentage(stat_name, stat_index_main, stat_index_b, stat_index_c):

        sysme = ""
        while True:
            initialise_screen(6)
            print(f"{t()}    {stat_name} Percentage\n")
            show_table_stats()
            print(f"\n{sysme}")
            selected_team = input(f"{t()}please select team (press 'q' to quit): ")
            if selected_team == "q":
                break
            elif selected_team in list(table_stats):
                sleep(1)
                win_percentage = (
                    table_stats[selected_team][stat_index_main]
                    / (
                        table_stats[selected_team][stat_index_main]
                        + table_stats[selected_team][stat_index_b]
                        + table_stats[selected_team][stat_index_c]
                    )
                ) * 100
                sysme = f"{t()}{selected_team} {stat_name.lower()} percentage: {win_percentage}\n"

            else:
                for x in list(table_stats):
                    if selected_team == x[:3]:
                        sleep(1)
                        win_percentage = (
                            table_stats[x][stat_index_main]
                            / (
                                table_stats[x][stat_index_main]
                                + table_stats[x][stat_index_b]
                                + table_stats[x][stat_index_c]
                            )
                        ) * 100
                        sysme = f"{t()}{x} {stat_name.lower()} percentage: {win_percentage}\n"

    def show_stat(stat_name, stat_index):

        print(f"{t()}Team {stat_name}: \n")
        count = 1
        for x, y in table_stats.items():
            print(f"{t()}{count}. {x}: {y[stat_index]}")
            count += 1

    def menu_prompt():

        main_menu = input(f"\n{t()}back to main menu?  [y] [n]  ")
        if main_menu == "y":
            menu()
        elif main_menu == "n":
            print(f"\n{t()}exit... ")
        else:
            print(f"... ")

    def menu():

        while True:
            initialise_screen(16)
            menu_items = [
                "show table stats",
                "win percentage",
                "draw percentage",
                "loss percentage",
                "show wins",
                "show draws",
                "show losses",
                "goals for",
                "goals against",
                "quit",
            ]
            count = 1
            for item in menu_items:
                print(f"{t(7)}{count}. {item}\n")
                count += 1

            input_item = input(f"{t(7)}select menu option: ")
            if input_item == "1":
                initialise_screen(6)
                show_table_stats()
                menu_prompt()
                break
            elif input_item == "2":
                show_stat_percentage("Win", 0, 1, 2)
            elif input_item == "3":
                show_stat_percentage("Draw", 1, 0, 2)
            elif input_item == "4":
                show_stat_percentage("Loss", 2, 0, 1)
            elif input_item == "5":
                initialise_screen(6)
                show_stat("Wins", 0)
                menu_prompt()
                break
            elif input_item == "6":
                initialise_screen(6)
                show_stat("Draws", 1)
                menu_prompt()
                break
            elif input_item == "7":
                initialise_screen(6)
                show_stat("Losses", 2)
                menu_prompt()
                break
            elif input_item == "8":
                initialise_screen(6)
                show_stat("Goals For", 3)
                menu_prompt()
                break
            elif input_item == "9":
                initialise_screen(6)
                show_stat("Goals Against", 4)
                menu_prompt()
                break
            elif input_item == "10":
                break

    menu()

    n(2)


name()
