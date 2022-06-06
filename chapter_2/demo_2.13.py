# Chapter 2
# 2.5 Exercises
# 13.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)
    
    height = eval(input("enter height: "))
    
    n()
    for x in range(height):
        print(f'{"*" * height}')
        height -= 1

    n(2)

main()
