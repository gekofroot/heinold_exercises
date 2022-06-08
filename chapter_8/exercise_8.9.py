# Chapter 8
# 8.7 Exercises
# 9.

from random import choice, randint
from os import system
from time import sleep, strftime


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():

    questions = [
        "what is one plus one?",
        "what is the fastest car in North America?",
        "what is the capital of France?",
        "what 6 x 3?",
        "what is a female deer called?",
        "how many letters does the english alphabet contain?",
        "who won the World Cup in 2014?",
        "in what year do secondary students generally graduate?",
        "is 53 a perfect number?",
        "how do plants get energy from the sun?",
        "where do dolphins live?",
    ]

    answers = [
        "2",
        "Volkswagon Beetle",
        "Paris",
        "18",
        "doe",
        "26",
        "Germany",
        "12",
        "no",
        "photosynthesis",
        "the ocean",
    ]

    selected = []
    selected_ans = []

    count_3 = 0
    quesnum = len(questions)
    quesnum = 4
    while count_3 < quesnum:
        count = randint(0, len(questions) - 1)
        count_2 = len(questions)
        sel = questions[count]
        sel_ans = answers[count]
        if sel not in selected:
            selected.append(sel)
            selected_ans.append(sel_ans)
            questions.remove(questions[count])
            answers.remove(answers[count])
            count = randint(0, count_2 - 1)
            count_3 += 1
        else:
            print("selected already contains:", sel)

    counter_4 = 0
    correct = 0
    incorrect = 0
    for x in selected:
        n(6)
        date = print(strftime(f"%A %B %d %Y"))
        dlm(22)
        n()
        print(x)
        n()
        ans = input("answer? ")
        ans = ans.strip()
        ansform = [ans.lower(), ans.upper(), ans.title(), ans.capitalize()]
        if selected_ans[counter_4] in ansform:
            print("correct")
            correct += 1
        else:
            print("incorrect")
            print("answer is:", selected_ans[counter_4])
            incorrect += 1
        n(1)
        sleep(4)
        system("clear")
        counter_4 += 1

    n(6)
    date = print(strftime(f"%A %B %d %Y"))
    dlm(22)
    n()
    print("you got", correct, "answers right out of", quesnum)

    perc = (correct / quesnum) * 100
    print(f"score: {perc:.0f}%")

    if perc == 100:
        print("well done")
    elif 100 < perc >= 80:
        print("good job")
    elif 80 <= perc:
        print("alright")
    elif 75 <= perc:
        print("passable")
    elif 50 <= perc:
        print("needs improvement")
    elif perc <= 30:
        print("... ")

    n(2)


name()
