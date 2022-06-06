# Chapter 3
# 3.8
# 11.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    weight_in_kg = eval(input(f'please enter weight in kilograms: '))

    weight_in_pounds = round((weight_in_kg / 2.20462262185), 2)

    print(f'\nweight in pounds: {weight_in_pounds}')

    n(2)

main()
