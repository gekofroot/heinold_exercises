# Chapter 6
# 6.11 Exercises
# 1.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    dlm(70)
    n(1)

    s = input("please enter a string: ")

    print("character total:", len(s))
    n(1)
    print("string x 10:", s * 10)
    n(1)
    print("first character:", s[0])
    n(1)
    print("first three characters:", s[:3])
    n(1)
    print("last three characters:", s[-3:])
    n(1)

    # reverse_string = ''

    # for i in range(1, 2):
    #    while i <= len(s):
    #        reverse_string += s[-i]
    #        i += 1

    # print("string backwards:", reverse_string)
    print("string backwards", s[::-1])
    n(1)
    if len(s) >= 7:
        print("seventh character:", s[7])
    else:
        print("this sentence has less than seven characters")
    n(1)
    print("first and last characters removed:", s[1:-1])
    n(1)
    print("string in all caps:", s.upper())
    n(1)

    for i in "a":
        s = s.replace(i, "e")
    print("every a replaced with e:", s)
    n(1)

    for i in s:
        s = s.replace(i, " ")

    print("every letter replaced with a space:", s)

    n(2)


name()
# Chapter 5
# 5.9 Exercises
# 1.
