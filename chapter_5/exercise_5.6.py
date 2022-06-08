# Chapter 5
# 5.9 Exercises
# 6.

def n(x=0):
    print("\n" * x)


def perfect_numbers(top_range):
    n(1)

    perfect_numbers = []

    def get_divisors(number):

        divisors = []

        for divisor in range(1, number):
            if number / divisor % 1 == 0:
                divisors.append(divisor)

        if sum(divisors) == number:
            perfect_numbers.append(number)

    def count_divisors(top_range):

        for number in range(1, top_range + 1):
            get_divisors(number)

        print(f"perfect numbers between 1 - {top_range} {perfect_numbers}")
        n(2)

    count_divisors(top_range)


perfect_numbers(10000)
