# Chapter 2
# 2.5 Exercises
# 3.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    name = input("enter name: ")
    number = eval(input("enter number: "))
    
    count = 0
    for x in range(number):
        print(f'{count}. {name}')
        count += 1

    n(2)

main()
