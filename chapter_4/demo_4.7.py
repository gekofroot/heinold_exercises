# Chapter 4
# 4.5 Exercises
# 7.

def number_near():

    input_number_1 = float(input("Please enter a number: "))

    input_number_2 = float(input("Please enter a second number: "))

    if input_number_2 - input_number_1 <= 0.001:
        print("Close")
    else:
        print("Not close.")

number_near()
