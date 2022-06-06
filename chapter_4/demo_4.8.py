# Chapter 4
# 4.5
# 8.

def get_leap_year():

    input_year = int(input("Please enter the year: "))

    if input_year % 4 == 0:
        if input_year % 100 == 0:
            if input_year % 100 == 0 and input_year % 400 == 0:
                print(askyear, "is a leap year.")
            else:
                print(input_year, "is not a leap year.")
        else:
            print(input_year, "is a leap year.")
    else:
        print(input_year, "is not a leap year.")

get_leap_year()
