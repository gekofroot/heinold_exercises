# Chapter 3
# 3.8 Exercises
# 12.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    number = eval(input('enter a number: '))

    def get_factorial(x):
        factorial = 1
        for num in range(1, x + 1):
            factorial *= num
        return factorial

    print(f'\nfactorial of {number} is {get_factorial(number)}')

    n(2)

main()
