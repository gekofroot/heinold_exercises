# chapter 5
# 5.9 exercises
# 9.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def perfnum():
    n(1)

    squares = []
    perfect_squares = []
    non_perfect_squares = []

    cubes = []
    perfect_cubes = []
    non_perfect_cubes = []

    fifths = []
    perfect_fifths = []
    non_perfect_fifths = []

    number = eval(input(f"please enter number: "))

    a = 1

    def get_perfect_number(append_to, pwr, append_to_2, append_to_3):

        for divisor in range(a, number):
            result = divisor ** pwr
            append_to.append(result)

        for x in range(a, number):
            for divisor in range(a, x):
                if divisor ** pwr == x:
                    append_to_2.append(x)
                elif x not in append_to:
                    if x not in append_to_3:
                        append_to_3.append(x)

    get_perfect_number(squares, 2, perfect_squares, non_perfect_squares)

    get_perfect_number(cubes, 3, perfect_cubes, non_perfect_cubes)

    get_perfect_number(fifths, 5, perfect_fifths, non_perfect_fifths)

    n()
    print(f"perfect squares: {perfect_squares}")
    n()
    print(
        f"there are {len(perfect_squares)} perfect squares in the range of {a} - {number}"
    )
    n()
    # print(f'non perfect squares: {non_perfect_squares}')
    # n()
    # print(f'there are {len(non_perfect_squares)} non perfect squares in the range of {a} - {number}')
    n(1)

    print(f"perfect cubes: {perfect_cubes}")
    n()
    print(
        f"there are {len(perfect_cubes)} perfect cubes in the range of {a} - {number}"
    )
    n()
    # print(f'non perfect cubes: {non_perfect_cubes}')
    # n()
    # print(f'there are {len(non_perfect_cubes)} non perfect cubes in the range of {a} - {number}')
    n(1)

    print(f"perfect fifths: {perfect_fifths}")
    n()
    print(
        f"there are {len(perfect_fifths)} perfect fifths in the range of {a} - {number}"
    )
    n()
    # print(f'non perfect fifths: {non_perfect_fifths}')
    # n()
    # print(f'there are {len(non_perfect_fifths)} non perfect fifths in the range of {a} - {number}')

    n(2)


perfnum()
