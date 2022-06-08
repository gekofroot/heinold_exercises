# Chapter 7
# 7.7 Exercises
# 8.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    num = eval(input("please enter an integer: "))

    n()
    nums = []
    for x in range(1, num + 1):
        nums.append(x)
        print(x)
    n()
    print("factorials of", num, "are:", nums)

    index = 1
    count = 1
    while count < len(nums):
        n()
        for x in nums:
            print(index, "*", count)
            y = index * count
            index = y
            count += 1
            print(y)

    n(2)


name()
