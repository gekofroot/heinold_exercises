# Chapter 8
# 8.7 Exercises
# 10.

from string import punctuation


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sen = input(
        "please enter a sentence. \n we encourage you to keep your language appropriate: "
    )

    for c in punctuation:
        sen = sen.replace(c, "")
    ssen = sen.split()

    swords = ["darn", "dang", "freakin", "heck", "shoot"]

    count = 0
    print("ssen:", ssen)
    for x in ssen:
        print("word:", x, swords)
        if x in swords:
            print("issword:", ssen[count])
            ssen[count] = "*" * len(ssen[count])
        count += 1

    ssen = " ".join(ssen)

    sen_f = ""
    for x in ssen:
        sen_f += x
    sen_f += "."
    n(2)
    print(sen_f)

    n(2)


name()
