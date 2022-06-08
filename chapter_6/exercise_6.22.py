# Chapter 6
# 6.11 Exercises
# 22.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    # sen  = input("please enter a string: ")
    sen = "message"

    def encr():

        sen_n = ""

        sen_e = sen[::2]
        sen_o = sen[1::2]
        sen_n += sen_e
        sen_n += sen_o

        print(sen_n)

    encr()

    def decr():
        sen = "msaeesg"
        # print(
        sen_un = ""
        count = 0

        sen_e = sen[:4]
        print("sen_e:", sen_e)
        sen_o = sen[4:]
        print("sen_o:", sen_o)

        for x in range(0, len(sen) + 1):
            if count < len(sen_e):
                print("sen_e:", sen_e[count])
                sen_un += sen_e[count]
                print("sen_un:", sen_un)
                n()
            if count < len(sen_o):
                print("sen_o:", sen_o[count])
                sen_un += sen_o[count]
                print("sen_un:", sen_un)
                n()
            count += 1

        print(sen_un)

    decr()

    n(2)


name()
