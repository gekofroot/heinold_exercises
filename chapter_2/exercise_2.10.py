# Chapter 2
# 2.5 Exercises
# 10.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    width = eval(input("enter width: "))
    height = eval(input("enter height: "))

    n()
    for x in range(height):
        print(f'{"* " * width}')

    n(2)

main()
