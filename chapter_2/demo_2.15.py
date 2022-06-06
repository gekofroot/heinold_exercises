# Chapter 2
# 2.5 Exercises
# 15.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    letter_height = eval(input("enter letter size: "))

    n()
    count = 1
    space = letter_height
    print(f'{" " * space} *')
    for x in range(letter_height):
        print(f'{" " * space}*{" " * count}*')
        if x == (letter_height // 2) - 1:
            print(f'{" " * (space - 1)}*{"*" * (count + 2)}*')
            count += 2
            space -= 1
        count += 2
        space -= 1

    n(2)

main()
