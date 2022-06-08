# Chapter 6
# 6.11 Exercises
# 12.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


# def name():
#    n(1)
#
#    sen = input("please enter a word: ")
#
#    word = []
#    for x in sen:
#        word.append(x)
#
#    word_mod = ''
#
#    n()
#    count = 0
#    for x in word:
#        if count % 2 == 0:
#            word_mod += word[count]
#        elif count % 2 == 1:
#            word[count] = word[count].capitalize()
#            word_mod += word[count]
#        count += 1
#
#    print(word_mod)
#
#
#
#    n(2)
#
#
#
# name()


def name():
    n(1)

    sen = input("please enter a word: ")

    sen_m = ""

    sen_l = sen[::2]
    sen_u = sen[1::2].upper()

    count = 0
    for x in range(0, len(sen) + 1):
        if count < len(sen_l):
            sen_m += sen_l[count]
        if count < len(sen_u):
            sen_m += sen_u[count]
        count += 1

    n()
    print(sen_m)

    n(2)


name()
