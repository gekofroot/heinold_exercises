# Chapter 2
# 2.5 Exercises
# 12.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    height = eval(input("enter height: "))
    
    n()
    count = 1
    for x in range(height):
        print(f'{"*" * count}')
        count += 1

    n(2)

main()
