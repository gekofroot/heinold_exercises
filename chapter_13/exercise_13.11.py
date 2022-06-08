# Chapter 3
# 13.6 Exercises
# 11.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    first_string = input("string 1: ")
    second_string = input("string 2: ")

    def matches(string_1, string_2):

        string_list_1 = []
        string_list_2 = []
        for x in string_1:
            string_list_1.append(x)
        for x in string_2:
            string_list_2.append(x)

        range_length_1 = len(string_list_1)
        range_length_2 = len(string_list_2)
        if range_length_1 <= range_length_2:
            range_length = range_length_1
        else:
            range_length = range_length_2

        matches = 0
        matching_characters = []
        count = 0
        for x in range(range_length):
            if string_list_1[count] == string_list_2[count]:
                matching_characters.append(string_list_1[count])
                matches += 1
            count += 1

        print(f"\nthere are {matches} matching characters between the two strings")
        print(f"matching characters: {matching_characters}")

    matches(first_string, second_string)

    n(2)


name()
