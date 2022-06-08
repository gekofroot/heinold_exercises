# Chapter 6
# 6.11 Exercises
# 15.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    verb = input("please enter a verb: ")
    adjective = input("please enter an adjective: ")
    noun = input("please enter a noun(place): ")
    verb_2 = input("second verb: ")
    adjective_2 = input("second adjective: ")
    noun_2 = input("second noun{thing): ")

    n()
    print(
        "I", verb, "to the", adjective, noun, "to", verb_2, "some", adjective_2, noun_2
    )

    n(2)


name()
