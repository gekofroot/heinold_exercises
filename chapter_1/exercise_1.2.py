# Chapter 1
# 1.8 Exercises
# 2.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    print('*' * 20)
    for x in range(2):
        print(f'*{" " * 18}*')
    print('*' * 20)

    n(2)

main()
