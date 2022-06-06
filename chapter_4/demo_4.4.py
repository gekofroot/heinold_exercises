# Chapter 4
# 4.5 Exercises
# 4.

def get_credits():

    ask_credits = int(input("How many credits have you taken? "))

    if ask_credits <= 23:
        if ask_credits == 1:
            print("With", ask_credits, "credit, you are a freshman.")
        else:
            print("With", ask_credits, "credits, you are a freshman.")
    elif 24 < ask_credits < 53:
        print("With", ask_credits, "credits, you are a sophmore.")
    elif 54 < ask_credits < 83:
        print("With", ask_credits, "credits, you are a junior.")
    elif ask_credits > 84:
        print("With", ask_credits, "credits, you are a senior.")
    else:
        print("Please enter the amount of credits you have.")

get_credits()
