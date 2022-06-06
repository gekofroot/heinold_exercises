# Chapter 4
# 4.5 Exercises
# 12.

def guess_number():

    estimate_1 = []
    estimate_2 = []
    estimate_3 = []
    estimate_4 = []

    for number in range(0, 200):
        if (number % 5) == +2:
            # print(n / 5 == 2)
            print("True 1 for: ", number)
            estimate_1.append(number)

        if (number % 6) == +3:
            # print(n / 6 == 3)
            print("True 2 for: ", number)
            estimate_2.append(number)

        if (number % 7) == +2:
            # print(n / 7 == 2)
            print("True 3 for: ", number)
            estimate_3.append(number)

        # elif int(number) < 200:
        #    #print(number)
        #    print("True 4 for: ", number)
        #    estimate_4.append(number)

    print("estimate_1: ", estimate_1)
    print("estimate_2: ", estimate_2)
    print("estimate_3: ", estimate_3)
    # print("estimate_4: ", estimate_1)

    # print(estimate_4)

guess_number()
