# Chapter 3
# 13.6 Exercises
# 13.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sen = input(f"please enter a string: ")

    def change_case(string):

        print(f"\nstring: {string}")
        string_list = []
        for x in string:
            string_list.append(x)

        count = 0
        for item in string_list:
            if item == item.upper():
                string_list[count] = item.lower()
            if item == item.lower():
                string_list[count] = item.upper()
            count += 1
        string = ""
        for x in string_list:
            string += x
        print(f"\nstring case change: {string}")

    change_case(sen)

    n(2)


name()
