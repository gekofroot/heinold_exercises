# Chapter 6
# 6.11 Exercises
# 13.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sen_1 = input("please enter first string: ")
    # sen_1 = "ABCD"
    sen_2 = input("please enter second string: ")
    # sen_2 = "abcd"
    n()

    sen_mod = ""

    count = 0
    if len(sen_1) != len(sen_2):
        print("strings not equal length")
    else:
        for x in sen_1:
            sen_mod += sen_1[count]
            sen_mod += sen_2[count]
            count += 1

    print("alternated characters:", sen_mod)

    n(2)


name()
