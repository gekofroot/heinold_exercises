
# Chapter 5
# 5.9 Exercises
# 2.

def square_number(number_a, number_b):

    print("\n")

    squares = []

    end_in_4 = []

    end_in_9 = []

    # find squares
    for number in range(number_a, number_b):
        for divisor in range(number_a, number):

            if number / divisor == divisor:
                squares.append(number)

    print(f"square numbers from {number_a} - {number_b}: {squares} \n")

    # return numbers ending in 4, 9
    for number in squares:
        if number % 10 == 4:
            end_in_4.append(number)
        elif number % 10 == 9:
            end_in_9.append(number)

    print(f"square numbers from {number_a} - {number_b} ending in 4 {end_in_4} \n")
    print(f"square numbers from {number_a} - {number_b} ending in 9 {end_in_9} \n")


square_number(1, 1000)
