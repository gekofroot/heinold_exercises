# Chapter 14
# 14.6 Exercises
# 1.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)



def name():
    n(1) 

    class Investment:

        def __init__(self, principle, interest):
            self.principle = principle
            self.interest = interest

        def value_after(self, years):
            return self.principle * (1 + (self.interest / 100)) * years

        def __str__(self):
            return 'Principle - {}, Interest rate - {}'.format(self.principle, self.interest)
    
    value_a = eval(input(f'principle investment: '))
    value_b = eval(input(f'interest rate: '))
    value_c = eval(input(f'years: '))
    
    investment = Investment(value_a, value_b)
    print(f'principle investment after {value_c} years: ${investment.value_after(value_c):.2f}')


    n(2)


name()
