# Chapter 3
# Exercises 3.8
# 8.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    number_of_seconds = eval(input(f'enter number of seconds: '))
    
    minutes = number_of_seconds // 60
    seconds = number_of_seconds % 60
 
    print(f'\n{number_of_seconds} seconds is {minutes} minutes and {seconds} seconds')

    n(2)

main()
