# Chapter 5
# 5.9 Exercises
# 4.

def n(x=0):
    print("\n" * x)


def compute_sum():

    initial_number = 1
    proceeding_number = 2

    count = 0
    for x in range(0, 1000):
        result = initial_number - proceeding_number
        initial_number += 2
        result + initial_number
        print(result + initial_number)
        proceeding_number += 2
        count += 1

    n(2)


compute_sum()
# Chapter 5
# 5.9 Exercises
# 1.
