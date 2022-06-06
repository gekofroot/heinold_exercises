# Chapter 1
# 1.8 Exercises
# 5.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    get_number = eval(input("number: "))
    print('the square of ', get_number, ' is ', get_number * get_number, '.', sep='')

    n(2)

main()
