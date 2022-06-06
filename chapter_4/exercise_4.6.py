# Chapter 4
# 4.5 Exercises
# 6.

def item_purchase():

    input_item = int(input("Please enter the number of items you'd like to buy. "))

    item_a = 12 * input_item

    item_b = 10 * input_item

    item_c = 7 * input_item

    if input_item < 10:
        print("Your total comes to,", item_a, "dollars")
    elif 10 < input_item < 99:
        print("Your total comes to,", item_b, "dollars.")
    elif input_item >= 100:
        print("Your total comes to,", item_c, "dollars.")
    else:
        print("Your total comes to 0 dollars.")

item_purchase()
