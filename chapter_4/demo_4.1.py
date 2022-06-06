# Chapter 4
# 4.5 Exercises
# 1.

def convert_centimeter():
    
    ask_centemeter = int(input("Please enter a length in centimeters. "))

    inches = ask_centemeter / 2.54

    if ask_centemeter < 0:
        print("Invalid entry...")
    else:
        print(ask_centemeter, "is", inches, "inches")

convert_centimeter()
