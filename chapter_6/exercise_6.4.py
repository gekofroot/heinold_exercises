# Chapter 6
# 6.11 Exercises
# 4.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sen = input("please enter a word: ")

    vowels = []

    consonants = []

    for x in sen:
        if x in "abcdfghjklmnpqrstvwxyz":
            consonants.append(x)
        elif x in "aeiou":
            vowels.append(x)

    if len(vowels) > 0:
        print(sen, "contains vowels", vowels)
    else:
        print(sen, "does not contain any vowels")

    if len(consonants) > 0:
        print(sen, "contains consonants", consonants)
    else:
        print(sem, "does not contain any consonants")

    # print("word contains", len(consonants), "consonants")
    # print("word contains", len(vowels), "vowels")

    n(2)


name()
