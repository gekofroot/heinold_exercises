# Chapter 3
# 3.8 Exercises
# 10.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    power = eval(input(f'enter a power: '))
    how_many_digits = eval(input(f'how many digits do you want? [1] [2] ')) 
    
    if how_many_digits == 1:
        last_digit = (2 ** power) % 10
        print(f'\nthe last digit of 2 ^ {power} is {last_digit}')
    elif how_many_digits == 2:
        last_two_digits = (2 ** power) % 100
        print(f'\nthe last two digits of 2 ^ {power} are {last_two_digits}')

    n(2)

main()
