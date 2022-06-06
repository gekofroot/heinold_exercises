# Chapter 3
# 3.8 Exercises
# 6.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    number_1 = eval(input(f'number 1: '))
    number_2 = eval(input(f'number 2: '))

    solution = (number_1 - number_2) / (number_1 + number_2)

    print(f'solution: {solution}')

    n(2)

main()
