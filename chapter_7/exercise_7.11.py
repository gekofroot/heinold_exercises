# Chapter 7
# 7.7 Exercises
# 11.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    num = []

    nums = [1]

    num_s = []

    count = 0
    for x in range(11):
        num_s.append([0] * count)
        count += 1

    count = 0
    for x in range(11):
        num.append(nums[0])
        for x in num_s[count]:
            num.append(x)
        count += 1

    print(num)

    n(2)


name()
