# Chapter 8
# 8.7 Exercises
# 12.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    num = input("please enter phone number: ")
    arcos = [780, 587, 933]
    n()
    count = 0
    if len(num) == 12:
        print("select 1")
        val_coun = 0
        num = num.split()
        num_jn = "-".join(num)
        coun_lis = [3, 3, 4]
        for x in range(3):
            if len(num[count]) == coun_lis[count]:
                for y in arcos:
                    if str(y) in str(num[0]):
                        val_coun += 1
            else:
                continue
            count += 1

        if val_coun != 3:
            afd = 1
            # continue
            print(num_jn, "is not a valid number")
        else:
            print(num_jn, "is a valid number")
    elif len(num) == 14:
        print("select 2")
        val_coun_b = 0
        num = num.split()
        num_jn = "-".join(num)
        coun_lis_ext = [1, 3, 3, 4]
        for x in range(4):
            if len(num[count]) == coun_lis_ext[count]:
                for y in arcos:
                    print(y)
                    print("yala")
                    if str(y) in str(num[1]):
                        val_coun_b += 1
            else:
                continue
            count += 1
        if val_coun_b != 4:
            print(num_jn, "is not a valid number")
        else:
            print(num_jn, "is a valid number")
    else:
        print("select 3")
        num = num.split()
        num_jn = "-".join(num)
        print(num_jn, "is not a valid number")

    n(2)


name()
