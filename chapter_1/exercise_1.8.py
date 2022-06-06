# Chapter 1
# 1.8 Exercises
# 8.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    number_1 = eval(input("enter number 1: "))
    number_2 = eval(input("enter number 2: "))
    number_3 = eval(input("enter number 3: "))

    total = number_1 + number_2 + number_3
    average = total / 3

    print(f'\nsum: {total}')
    print(f'average: {average}')

    n(2)

main()
