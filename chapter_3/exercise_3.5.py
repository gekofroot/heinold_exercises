# Chapter 3
# 3.8 Exercises
# 5.

from random import randint

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)
    
    number_list = []
    count = 2
    for x in range(50):
        number_list.append(randint(1, count))
        count += 1

    print(f'number list: {number_list}')

    n(2)

main()
