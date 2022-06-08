# Chapter 9
# 9.6 Exercises
# 7b.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sen = input("please enter a sentence: ")
    let = input("please enter a letter: ")
    indxof = 0
    for x in range(len(sen)):
        if let in sen:
            indxof = 1
            print(let, "at index:", sen.index(let))
            break

    if indxof == 0:
        print(let, "not in sentence")

    n(2)


name()
