# Chapter 5
# 5.9 Exercises
# 5.

def n(x=0):
    print("\n" * x)


def sum_of_divisor():
    n(1)

    divisor = []

    input_number = eval(input(f"please enter a number: "))

    # find divisors
    for number in range(1, input_number):
        if input_number / number % 2 == 0:
            divisor.append(number)

    print(f"\ndivisors of {input_number} {divisor}\n")
    print(f"sum of divisors of {input_number}: {sum(divisor)}")

    n(2)


sum_of_divisor()
