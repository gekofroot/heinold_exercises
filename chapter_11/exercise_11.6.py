# Chapter 11
# 11.5 Exercises
# 6.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    table_stats = {}
    score = {}

    while True:
        team_1 = input("team name 1: ")
        if team_1 == "q":
            break
        else:
            score_1 = eval(input("team score 1: "))

            team_2 = input("team name 2: ")
            score_2 = eval(input("team score 2: "))

            score[team_1] = score_1
            score[team_2] = score_2

            if score_1 > score_2:
                table_stats[team_1] = ["win"]
                table_stats[team_2] = ["loss"]
            elif score_1 < score_2:
                table_stats[team_1] = ["loss"]
                table_stats[team_2] = ["win"]
            elif score_1 == score_2:
                table_stats[team_1] = ["tie"]
                table_stats[team_2] = ["tie"]

    n()
    # print(table_stats)

    # for team_name, game_result in table_stats.items():
    #    print(f'{team_name}: {game_result}')

    count = 0
    while count < len(table_stats):
        print(
            f"{list(table_stats)[count]}: {list(score.values())[count]} {list(table_stats.values())[count]}"
        )
        count += 1
        n()

    n(2)


name()
