# Chapter 3
# 13.6 Exercises
# 2.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    words = input(f"please enter a list of strings: ")
    words = words.split()

    def add_exitement(string_list):

        print(f"\nstring list: {string_list}\n")
        count = 0
        for item in range(len(string_list)):
            string_list[count] = string_list[count] + "!"
            count += 1
        print(f"modified string list: {string_list}\n")

    add_exitement(words)

    words_2 = input(f"please enter a list of strings: ")
    words_2 = words_2.split()

    def add_exitement_2(string_list):

        new_string_list = []
        print(f"\nstring list: {string_list}\n")
        for item in string_list:
            item += "!"
            new_string_list.append(item)
        return new_string_list

    print(f"returned string list: {add_exitement_2(words_2)}")

    n(2)


name()
