# Chapter 3
# 3.8 Exercises
# 2.

from random import randint

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    x = randint(1, 50)
    y = randint(2, 5)
    comp = x ** y
    print(f'{x} ** {y} = {comp}')


    n(2)

main()
