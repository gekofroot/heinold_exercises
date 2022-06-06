# Chapter 3
# 1.8 Exercises
# 3.

def n(x=0):
    print("\n" * x)


def main():
    n(1)

    count = 0
    for x in range(5):
        print('*' * count)
        count += 1

    n(2)

main()
