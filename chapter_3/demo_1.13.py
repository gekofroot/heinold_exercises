# Chapter 3
# 3.8 Exercises
# 13.

from math import sin, cos, tan

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    number = eval(input('enter number: '))

    print(f'\nsin of {number} is {sin(number)}')
    print(f'cos of {number} is {cos(number)}')
    print(f'tan of {number} is {tan(number)}')

    n(2)

main()
