# Chapter 2
# 2.5 Exercises
# 2.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    name = input("enter name: ")
    number = eval(input("enter number: "))

    for x in range(number):
        print(name, end=' ')

    n(2)

main()
