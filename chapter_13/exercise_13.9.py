# Chapter 3
# 13.6 Exercises
# 9.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    def factors():

        number = eval(input("number: "))
        factors = []

        for divisor in range(1, number + 1):
            if number % divisor == 0:
                factors.append(divisor)

        print(f"\nthe number {number} is divisible by: {factors}")

    factors()

    n(2)


name()
