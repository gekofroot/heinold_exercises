# Chapter 4
# 4.5 Exercises
# 3.

def get_temperature():

    ask_temperature = int(input("Please enter the temperaturein celsius: "))

    if ask_temperature < -273.15:
        print(
            "The temperature",
            ask_temperature,
            "is invalid because it is below absolute 0.",
        )
    elif ask_temperature == -273.15:
        print("The temerature", ask_temperature, "is absolute 0.")
    elif -273.15 < ask_temperature < 0:
        print("The temperature", ask_temperature, "is below freezing.")
    elif ask_temperature == 0:
        print("The temperature", ask_temperature, "is at freezing point.")
    elif 0 < ask_temperature < 100:
        print("The temperature", ask_temperature, "is in the normal range.")
    elif ask_temperature == 100:
        print("Temperature", ask_temperature, "is at boiling point.")
    elif ask_temperature > 100:
        print("Temperature", ask_temperature, "is above boiling point.")

get_temperature()
