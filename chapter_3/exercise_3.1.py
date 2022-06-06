# Chapter 3
# 3.8 Exercises
# 1.

from random import randint

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    random_integers = [randint(3, 6) for x in range(50)]

    print(f'random integers: \n{random_integers}')
    
    n()
    count = 1
    for number in random_integers:
        print(f'number {count}: {number}')
        count += 1

    n(2)

main()
