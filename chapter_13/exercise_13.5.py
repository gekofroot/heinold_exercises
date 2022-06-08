# Chapter 3
# 13.6 Exercises
# 5.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    def first_off():

        first_string = input(f"please enter first string: ")

        second_string = input(f"please enter second string: ")

        list_first_string = []
        list_second_string = []

        for x in first_string:
            list_first_string.append(x)
        for x in second_string:
            list_second_string.append(x)

        differ_at_index = 0
        fs_differ_at_letter = 0
        ss_differ_at_letter = 0
        first_occurence = 0
        count = 0
        for x in range(len(list_first_string)):
            if list_first_string[count] != list_second_string[count]:
                differe_at_index = count
                fs_differ_at_letter = list_first_string[count]
                ss_differ_at_letter = list_second_string[count]
                first_occurence = 1
                break
            count += 1
        n()
        if first_occurence == 1:
            print(
                f"your first string differs at index {differ_at_index} with the letter {fs_differ_at_letter}\nwhile your second string differs at index {differ_at_index} with the letter {ss_differ_at_letter}"
            )
        else:
            print(f"-1")

    first_off()

    n(2)


name()
