# Chapter 2
# 2.5 Exercises
# 9.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    number = eval(input("enter number: "))

    n()
    a, b = 0, 1
    for x in range(number):
        print(a)
        a, b = b, a + b

    n(2)

main()
