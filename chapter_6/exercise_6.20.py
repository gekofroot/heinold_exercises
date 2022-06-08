# Chapter 6
# 6.11 Exercises
# 20.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    ent_tim_hou = eval(input("please enter hour: "))
    # ent_tim_hou = 10
    ent_tim_sec = eval(input("please enter seconds: "))
    # ent_tim_sec = 20
    ent_m = input("am/pm: ")
    # ent_m = "pm"
    timezones = ["eastern", "central", "mountain", "pacific"]
    print("\n")
    count = 0
    for timezone in timezones:
        print(f"{count}. {timezone}")
        count += 1
    print("\n")
    starting_timzon = input("please enter starting timezone: ")
    count = 0
    ending_timzon = input("please enter ending timezone: ")

    def get_timzone(
        timezone, timezone_b, ofst_a, timezone_c, ofst_b, timezone_d, ofst_c
    ):
        ent_tim_hou_b = 0
        ent_tim_hou_b += ent_tim_hou
        ent_m_b = ""
        ent_m_b += ent_m
        if timezone in starting_timzon:
            if timezone in ending_timzon:
                ent_tim_hou_b = ent_tim_hou_b
            elif timezone_b in ending_timzon:
                ent_tim_hou_b += ofst_a
                if ent_tim_hou_b > 12:
                    ent_tim_hou_b -= 12
                    if ent_m == "am":
                        ent_m_b = "pm"
                    elif ent_m == "pm":
                        ent_m_b = "am"
            elif timezone_c in ending_timzon:
                ent_tim_hou_b += ofst_b
                if ent_tim_hou_b > 12:
                    ent_tim_hou_b -= 12
                    if ent_m == "am":
                        ent_m_b = "pm"
                    elif ent_m == "pm":
                        ent_m_b = "am"
            elif timezone_d in ending_timzon:
                ent_tim_hou_b += ofst_c
                if ent_tim_hou_b > 12:
                    ent_tim_hou_b -= 12
                    if ent_m == "am":
                        ent_m_b = "pm"
                    elif ent_m == "pm":
                        ent_m_b = "am"
        n()
        print(
            "current time: ",
            ent_tim_hou,
            ":",
            ent_tim_sec,
            " ",
            ent_m,
            " ",
            starting_timzon.lower(),
            sep="",
        )
        print(
            "timezone change: ",
            ent_tim_hou_b,
            ":",
            ent_tim_sec,
            " ",
            ent_m_b,
            " ",
            ending_timzon.lower(),
            sep="",
        )

    if starting_timzon in "eastern":
        n()
        get_timzone(starting_timzon, "central", 1, "mountain", 2, "pacific", 3)
    elif starting_timzon in "central":
        n()
        get_timzone(starting_timzon, "eastern", -1, "mountain", 1, "pacific", 2)
    elif starting_timzon in "mountain":
        n()
        get_timzone(starting_timzon, "eastern", -2, "central", -1, "pacific", 1)
    elif starting_timzon in "pacific":
        n()
        get_timzone(starting_timzon, "eastern", -3, "central", -2, "mountain", -1)

    n(2)


name()
