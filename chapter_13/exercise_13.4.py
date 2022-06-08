# Chapter 3
# 13.6 Exercises
# 4.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    digits = input(f"please enter a digit: ")

    def digital_root(num):
        if len(num) == 1:
            print(f"the digital root of {digits} is {num}")
        else:
            while len(num) > 1:
                split_digits = []

                count = 0
                for x in range(len(num)):
                    split_digits.append(int(num[count]))
                    count += 1

                new_digits = 0
                for x in split_digits:
                    new_digits += x
                num = str(new_digits)
                if len(num) == 1:
                    print(f"\nthe digital root of {digits} is {num}")

    digital_root(digits)

    n(2)


name()
