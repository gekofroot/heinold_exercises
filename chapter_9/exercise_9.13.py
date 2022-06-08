# Chapter 9
# 9.6 Exercises
# 13.

from random import choice
from os import system
from time import sleep


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    sel = ["rock", "paper", "scissors"]

    global userscore
    global cmpscore
    global tie

    cmpscore = 0
    userscore = 0
    tie = 0

    def cmpw():
        global cmpscore
        cmpscore += 1
        print("\tcomputer wins\n")

    def usrw():
        global userscore
        userscore += 1
        print("\tuser wins\n")

    def tiesc():
        global tie
        tie += 1
        print("\ttie\n")

    sen_prm = input("overwrite existing: ")
    if sen_prm in "yes":
        print("overwriting exisiting: ")
        fln_2 = open("filename_2", "w")
        system('echo -e "\n\tnew game... " > filename_2')
    elif sen_prm in "no":
        print("appending to exisiting: ")
        system('echo -e "\n\tgame continue... " >> filename_2')

    outof = 2
    while cmpscore < outof and userscore < outof:

        n(3)
        print("\tbest out of:", outof)
        print("\tuser score:", userscore)
        print("\tcomputer score:", cmpscore)
        print("\ttie score:", tie)

        print("\tcomputer choice... ")
        cmpch = choice(sel)
        n()

        userch = input("\tuser choice... [rock] [paper] [scissors]: ")
        n()
        print("\tcomputer choice:", cmpch)
        n()
        if userch == "rock":
            if cmpch == "rock":
                tiesc()
            elif cmpch == "paper":
                cmpw()
            elif cmpch == "scissors":
                usrw()
        elif userch == "paper":
            if cmpch == "rock":
                usrw()
            elif cmpch == "paper":
                tiesc()
            elif cmpch == "scissors":
                cmpw()
        elif userch == "scissors":
            if cmpch == "rock":
                cmpw()
            elif cmpch == "paper":
                usrw()
            elif cmpch == "scissors":
                tiesc()
        else:
            print("invalid entry..")
            cmpw()

        fln = open("filename", "w")
        print("\n", file=fln)
        print("\tcomputer choice:", cmpch, file=fln)
        print("\tuser choice:", userch, "\n", file=fln)
        print("\tuser score:", userscore, file=fln)
        print("\tcomputer score:", cmpscore, file=fln)
        print("\ttie score:", tie, file=fln)
        fln.close()
        system("cat filename >> filename_2")
        sleep(2)
        system("clear")

    n(4)
    print("\tuser score:", userscore)
    print("\tcomputer score:", cmpscore)
    print("\ttie score:", tie)
    n()
    system("cat filename")

    if cmpscore > userscore:
        print("\n\tcomputer wins")
    elif userscore > cmpscore:
        print("\n\tuser wins")
    elif cmpscore == userscore:
        print("\n\ttie game")

    fln_2.close()
    system("cat filename_2")

    n(2)


name()
