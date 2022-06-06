# Chapter 2
# 2.5 Exercises
# 14.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    diamond_height = eval(input("enter diamond height: "))
    
    n()
    count = 1
    space = diamond_height
    for x in range(diamond_height):
        print(f'{" " * space}{"*" * count}')
        count += 2
        space -= 1
    for x in range(diamond_height + 1):
        print(f'{" " * space}{"*" * count}')
        count -= 2
        space += 1

    n(2)

main()
