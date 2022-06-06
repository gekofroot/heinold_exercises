# Chapter 4
# 4.5 Exercises
# 11.

def current_time():

    # initial hour
    get_hour = int(input("Please enter hour: "))
    # am or pm
    get_m = int(input("am (1) or pm (2)? "))
    # how many hours ahead
    get_hours_ahead = int(input("how many hours ahead? "))

    # newhour, ask hour plus askahead
    new_hour = get_hour + get_hours_ahead

    if get_m == 1:
        if get_hours_ahead > 12:
            print("New hour: ", (new_hour - 12), "pm")
        elif get_hours_ahead == 12:
            print("New hour: ", new_hour, "pm")
        else:
            print("New hour: ", (new_hour - 12), "pm")

    elif get_m == 2:
        if new_hour > 12:
            print("New hour: ", (new_hour - 12), "am")
        else:
            print("New hour: ", new_hour, "pm")

current_time()
