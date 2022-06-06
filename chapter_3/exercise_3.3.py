# Chapter 3
# 3.8 Exercises
# 3.

from random import randint

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    name = input("enter name: ")
    random_number = randint(1, 10)

    count = 1
    print(f'printing name {random_number} times\n')
    for x in range(random_number):
        print(f'{count}. {name}')
        count += 1

    n(2)

main()
