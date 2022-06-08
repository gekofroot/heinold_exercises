# Chapter 8
# 8.7 Exercises
# 1.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sen = input("please enter a string: ")

    articles = ["a", "an", "the"]
    count = 0
    for x in sen.split():
        if x in articles:
            count += 1

    print("there are", count, "articles in this sentence")

    n(2)


name()
