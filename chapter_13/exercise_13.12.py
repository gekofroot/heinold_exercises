# Chapter 3
# 13.6 Exercises
# 12.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sen = input("please enter a string: ")
    char = input("please select a character: ")

    def findall(string, character):

        string_list = []
        for x in string:
            string_list.append(x)

        times = 0
        index = []
        count = 0
        for x in range(len(string_list)):
            if string_list[count] == char:
                times += 1
                index.append(count)
            count += 1

        if times == 1:
            print(f"\nthe character {char} appears once in string at index: {index}")
        else:
            print(
                f"\nthe character {char} appears {times} times in string at index: {index}"
            )

    findall(sen, char)

    n(2)


name()
