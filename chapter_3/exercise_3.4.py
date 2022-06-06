# Chapter 3
# 3.8 Exercises
# 4.

from random import randint

def n(x=0):
    print("\n" * x)


def main():
    n(1)
    
    random_number = randint(1.00, 10.00)
    # float object cannot be interpreted as an integer
    print(f'{random_number:.2f}')

    n(2)

main()
