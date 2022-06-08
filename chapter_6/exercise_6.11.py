# Chapter 6
# 6.11 Exercises
# 11.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sen = input("please enter a word containing the letter 'a' : ")
    # sen = "buffalo"
    n()

    print("word:", sen)
    n()
    word = []

    first_a = []
    up_to = ""

    after = ""

    for x in sen:
        word.append(x)

    count = 0
    for x in sen:
        if sen[count] in "a":
            first_a.append(count)
        count += 1

    up_to = sen[: first_a[0] + 1]
    after = sen[first_a[0] + 1 :]

    print("word up to letter a:", up_to)
    print("word after letter a:", after)

    n(2)


name()
