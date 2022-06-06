# Chapter 3
# 3.8 Exercises
# 18.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    change_amount = eval(input(f'enter amount of change between 1 and 99: '))
    
    if change_amount >= 25:
        quarter_mod = change_amount // 25
        change_amount = change_amount - (25 * quarter_mod)
    else:
        quarter_mod = 0

    if change_amount >= 10:
        dime_mod = change_amount // 10
        change_amount = change_amount - (10 * dime_mod)
    else:
        dime_mod = 0

    if change_amount >= 5:
        nickel_mod = change_amount // 5
        change_amount = change_amount - (5 * nickel_mod)
    else:
        nickel_mod = 0
    
    if change_amount < 5:
        penny_mod = change_amount // 1
        change_amount = change_amount = (1 * penny_mod)
    else:
        penny_mod = 0

    print(f'\nyour change comes to {quarter_mod} quarters, {dime_mod} dimes, {nickel_mod} nickels, and {penny_mod} pennies')

    n(2)

main()
