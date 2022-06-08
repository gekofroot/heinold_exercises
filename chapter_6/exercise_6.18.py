# Chapter 6
# 6.11 Exercises
# 18.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name_a():
    n(1)

    sen = input("please enter a string: ")
    let = input("please enter a letter: ")

    count = 0

    sen_lis = []

    for x in sen:
        sen_lis.append(x)

    let_in_sen = ""

    for x in range(0, len(sen)):
        if let == sen[x]:
            let_in_sen += sen[x]

    n()
    if len(let_in_sen) > 0:
        print("letter", let, "appears in:", sen)
    else:
        print("letter", let, "does not appear in:", sen)

    n(2)


# name_a()


def name_b():
    n(1)

    s = input("please enter a string: ")
    let = input("please enter a letter: ")

    let_in_s = []

    for x in range(len(s)):
        print(x, s[x])
        if let == s[x]:
            let_in_s.append(s[x])

    print("the letter", let, "appears", len(let_in_s), "times in:", s)

    n(2)


# name_b()


def name_c():
    n(1)

    s = input("please enter a string: ")
    let = input("please enter a letter: ")

    first_occ = []
    let_in_s = []

    for x in range(0, len(s)):
        if let == s[x]:
            first_occ.append(x)

    if len(first_occ) > 0:
        print(
            "the first occurence of the letter",
            let,
            "in",
            s,
            "is at index",
            first_occ[0],
        )
    else:
        print("the letter", let, "does not appear in", s)

    n(2)

def menu():
    n(1)
    options = ["a. name_a", "b. name_b", "c. name_c", "q. quit"]
    for option in options:
        print(option)
    
    while True:
        select_option = input("select option: ")
        if select_option == "a":
            name_a()
        elif select_option == "b":
            name_b()
        elif select_option == "c":
            name_c()
        elif select_option == "q":
            break

menu()
# name_c()
