# Chapter 11
# 11.5 Exercises
# 3.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    months = {
        "January": 31,
        "Febuary": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }

    for key, value in months.items():
        print(f"{key}: {value}")

    n()
    while True:
        month = input("please select a month: ")
        if month == "q":
            break
        elif month in list(months):
            print(f"there are {months[month]} days in {month}")
        # else:
        #    print(f'the month {month} is not part of the calendar')
        for x in list(months):
            if month == x[:3]:
                print(f"there are {months[x]} days in {x}")

    months_alph = list(months)
    months_alph.sort()
    print(months_alph)

    for key, value in months.items():
        if value == 31:
            print(f"{key}: {value}")

    n(2)


name()
