# Chapter 4
# 4.5 Exercises
# 9.

def divisible_number():

    get_number = int(input("Please enter a number. "))
    for number in range(1, (get_number + 1)):
        if get_number % number == 0:
            print(get_number % number)
            print(get_number, "is divisible by", number, "\n")
        else:
            print(get_number % number)
            print(get_number, "is not divisible by", number, "\n")

divisible_number()
