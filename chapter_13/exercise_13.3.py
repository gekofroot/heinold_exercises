# Chapter 3
# 13.6 Exercises
# 3.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    digits = input("please enter an integer: ")

    def sum_digits(num):

        add_int = []
        count = 0
        for x in range(len(num)):
            add_int.append(int(num[count]))
            count += 1
        print(f"\nsum of {num} is {sum(add_int)}")

    sum_digits(digits)

    n(2)


name()
