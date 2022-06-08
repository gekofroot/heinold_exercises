# Chapter 11
# 11.5 Exercises
# 5.

from os import system
from time import sleep


def n(x=0):
    print("\n" * x)


def t(x=5):
    t = "\t" * x
    return t


def name():

    n(1)

    table_stats = {}

    teams = [
        "Manchester City",
        "PSG",
        "Leipzig",
        "Club Brugge",
        "Liverpool",
        "Atletico",
        "Porto",
        "Milan",
        "Ajax",
        "Sporting CP",
        "Dortmund",
        "Besiktas",
        "Real Madrid",
        "Inter",
        "Sherif",
        "Shaktar Donetsk",
        "Bayern",
        "Benifica",
        "Barcelona",
        "Dynamo Kayiv",
        "Manchester United",
        "Villareal",
        "Atalanta",
        "Young Boys",
        "LOSC",
        "Saizburg",
        "Sevilla",
        "Wolfsburg",
        "Juventus",
        "Chelsea",
        "Zenit",
        "Malmo",
    ]

    games_played = []
    for x in range(len(teams)):
        games_played.append(6)

    team_wins = [
        4,
        3,
        2,
        1,
        6,
        2,
        1,
        1,
        6,
        3,
        3,
        0,
        5,
        3,
        2,
        0,
        6,
        2,
        2,
        0,
        3,
        3,
        1,
        1,
        3,
        3,
        1,
        1,
        5,
        4,
        1,
        0,
    ]

    team_draws = [
        0,
        2,
        1,
        1,
        0,
        1,
        2,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        2,
        2,
        1,
        3,
        2,
        2,
        1,
        3,
        2,
        0,
        1,
        2,
        1,
        0,
        1,
        2,
        1,
    ]

    team_losses = [
        2,
        1,
        3,
        4,
        0,
        3,
        3,
        4,
        0,
        3,
        3,
        6,
        1,
        2,
        3,
        4,
        0,
        2,
        3,
        5,
        1,
        2,
        2,
        3,
        1,
        2,
        2,
        3,
        1,
        1,
        3,
        5,
    ]

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

    def show_stat(stat_name, stat_num):

        print(f"{t()}Team {stat_name}: \n")
        for x, y in table_stats.items():
            print(f"{t()} {x}: {y[stat_index]}")

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
                break

    menu()

    n(2)


name()
