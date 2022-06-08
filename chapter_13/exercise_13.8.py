# Chapter 3
# 13.6 Exercises
# 8.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    def number_of_factors():

        number = eval(input("number: "))
        factors = []
        nof = 0
        for divisor in range(1, number + 1):
            if number % divisor == 0:
                factors.append(divisor)
                nof += 1

        print(f"\nthe number {number} has {nof} factors: {factors}")

    number_of_factors()

    n(2)


name()
