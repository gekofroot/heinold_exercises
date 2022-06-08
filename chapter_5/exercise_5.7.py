# Chapter 5
# 5.9 Exercises
# 7.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def square_free():
    n(1)

    divisors = []
    square_free = 0

    input_number = eval(input(f"please enter a number: "))
    n()

    for divisor in range(1, input_number):
        if input_number / divisor % 1 == 0:
            divisors.append(divisor)

    for number in divisors:
        if square_free == 1:
            break
        for divisor in range(1, number):
            if number / divisor == divisor:
                print(number, "is a perfect square")
                square_free = 1

    n()
    if square_free == 1:
        print(input_number, "is not squarefree")
    else:
        print(input_number, "is squarefree")
    n(2)


square_free()
# Chapter 5
# 5.9 Exercises
# 7.
