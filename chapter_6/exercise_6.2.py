# Chapter 6
# 6.11 Exercises
# 2.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    num_of_spaces = 0

    sen = input("please enter a sentence: ")

    n()
    for x in sen:
        if " " == x:
            num_of_spaces += 1

    print(
        "there are aprroximately",
        num_of_spaces,
        "-",
        num_of_spaces + 1,
        "words in this sentence.",
    )

    n(2)


name()
