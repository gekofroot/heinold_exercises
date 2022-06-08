# Chapter 3
# 13.6 Exercises
# 6.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    value_a = eval(input("value a: "))
    value_b = eval(input("value b: "))

    def binom(digit_a, digit_b):
        def factorial(number):
            factorial = 1
            for x in range(1, number + 1):
                factorial *= x
            return factorial

        factorial_a = factorial(digit_a)
        factorial_b = factorial(digit_b)
        print(f"\nfactorial of {digit_a}: {factorial_a}")
        print(f"\nfactorial of {digit_b}: {factorial_b}")

        denom = factorial_b * (digit_a - digit_b)

        denom_factorial = factorial(denom)

        solution = factorial_a / denom_factorial

        print(f"\nbinoial coefficient: {solution}")

    binom(value_a, value_b)

    n(2)


name()
