# Chapter 9
# 9.6 Exercises
# 8.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


val_a = eval(input("please enter value a: "))
val_b = eval(input("please enter value b: "))


def name(num_a, num_b):
    n(1)
    if num_a > num_b:
        num_temp = num_a
        num_a = num_b
        num_b = num_temp

    def divby(num_a, num_b):
        o_num_a = num_a
        o_num_b = num_b
        remainder_of = 1
        remainder = 0
        mingcd = 0
        while remainder_of > 0:
            remainder = num_b % num_a
            if remainder > 0:
                remainder_of = num_a % remainder
            else:
                print("gcd is 0")
                mingcd = 1
                break
            n()

            num_b = remainder
            num_a = remainder_of

        if mingcd == 0:
            print("gcd of", o_num_b, "and", o_num_a, "is", num_b)

    divby(num_a, num_b)

    n(2)


name(val_a, val_b)
