# Chapter 9
# 1.8 Exercises
9.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    def tip_calculator():

        meal_price = float(input("meal price: "))
        tip = float(input("tip percent: "))

        tip_amount = (tip / 100) * meal_price
        meal_price_total = meal_price + tip_amount
        
        print(f'\ntip amount: {tip_amount}')
        print(f'meal_price_total: {meal_price_total}')

    tip_calculator()

    n(2)

main()
