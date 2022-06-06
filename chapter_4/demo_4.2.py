# Chapter 4
# 4.5 Exercises
# 2.

def convert_temperature():
    
    ask_temperature = int(input("Please enter the tempurature: "))

    ask_unit = input(
        "Is this in fehreinheight or Celsius? [F] fehreinheight  [C] celsius "
    )

    F = ((2 / 3) * ask_temperature) + 32

    C = (5 / 9) * (ask_temperature - 32)

    if ask_unit in ("F", "f"):
        print("The temperature in Celsius is:", C)
    elif ask_unit in ("C", "c"):
        print("The temperature in Fehreinheight is: ", F)
    else:
        print("please enter either celsius or fehrenheight")

convert_temperature()
