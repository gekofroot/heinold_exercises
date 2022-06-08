# Chapter 9
# 9.6 Exercises
# 5.

from os import system
from sys import argv


# def writeto():
#    sen = input("would you like to write to, or create new file: ")
#    if sen == 1:
#        script, filename = argv
#        f = open(filename, 'w')
#    elif sen == 2:
#        pass
# writeto()


testscores = open("text.txt", "r")
print(testscores.read())
testscores.close()

# f = open(filename, 'w')


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    test_name = []
    test_score = []

    def addItem():
        print("adding item")
        sen_2 = 1
        while sen_2 > 0:
            print("adding item")
            # print("type ^D to when done")
            sen = "testcore a"
            sen_2 = 20
            test_name.append(sen)
            test_score.append(sen_2)

            sen = "testcore b"
            sen_2 = 100
            test_name.append(sen)
            test_score.append(sen_2)

            sen = "testcore c"
            sen_2 = 50
            test_name.append(sen)
            test_score.append(sen_2)

            sen = "testcore d"
            sen_2 = 0

            # sen = input("please enter test name: ")
            # sen_2 = eval(input("please enter test score: "))
            test_name.append(sen)
            test_score.append(sen_2)

    def insertItem():
        num = 0
        while num >= 0:
            print("inserting item")
            sen_3 = "testcore e"
            sen_4 = 70
            num = 0
            test_name.insert(num, sen_3)
            test_score.insert(num, sen_4)

            sen_3 = "testcore f"
            sen_4 = 10
            num = 0
            test_name.insert(num, sen_3)
            test_score.insert(num, sen_4)

            sen_3 = "testcore g"
            sen_4 = 56
            num = 1
            test_name.insert(num, sen_3)
            test_score.insert(num, sen_4)

            sen_3 = "testcore h"
            sen_4 = 36
            num = -1

            # for x in range(len(test_name)):
            #    print(count, ": ", test_name[count], test_score[count])
            #    count += 1
            # sen_3 = input("please enter test name: ")
            # sen_4 = eval(input("please enter test score: "))
            # num = eval(input("please enter position in list: "))
            test_name.insert(num, sen_3)
            test_score.insert(num, sen_4)
            # count = 0
            # for x in range(len(test_name)):
            #    print(count, ": ", test_name[count], test_score[count])
            #    count += 1
            # x = f'{count}, ": ", {test_name[count]}, {test_score[count]}'
            # count = 0
            # f = open(filename, 'w')
            # print(count, ": ", test_name[count], test_score[count], file=f)

    def menu():
        sel = eval(
            input("would you like to add or insert items  [1] add  [2] insert  : ")
        )
        if sel == 1:
            addItem()
        elif sel == 2:
            insertItem()
        else:
            print("please select an available option")
            menu()

    menu()

    n()
    f = open("filename", "w")
    count = 0
    for x in range(len(test_name)):
        print("\n\n\n\n\n")
        print(f"{count}. {test_name[count - 1]}: {test_score[count - 1]}", file=f)
        count += 1
    f.close()
    system("cat filename >> text.txt")
    # count = 1
    # for x in range(len(test_name)):
    #    f = open(filename, 'w')
    #    print(count, ": ", test_name[count - 1], " ", test_score[count - 1], sep = '', file=f)
    #    count += 1

    testscores = open("text.txt", "r")
    print(testscores.read())
    testscores.close()
    n(2)


name()
