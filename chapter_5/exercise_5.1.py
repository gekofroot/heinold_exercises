# Chapter 5
# 5.9 Exercises
# 1.

def square_number(number_a, number_b):

    squares = []

    end_in_1 = []

    # find squares
    for x in range(number_a, number_b):
        for divisor in range(number_a, x):

            if x / divisor == divisor:
                squares.append(x)

    print(f"square numbers from {number_a} - {number_b} are: {squares} \n")

    # return numbers ending in 1
    for number in squares:
        if number % 10 == 1:
            end_in_1.append(number)

    print(f"squares from {number_a} - {number_b} that end in one are: {end_in_1} \n")


square_number(1, 1000)
