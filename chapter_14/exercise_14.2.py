# Chapter 14
# 14.6 Exercises
# 2.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)



def name():
    n(1)
    
    class Product:

        def __init__(self, name, amount, price):
            self.name = name
            self.amount = amount
            self.price = price

        def get_price(self, bought):
            
            if bought < 10:
                return self.price * bought
            elif 10 <= bought < 99:
                discount = (10 / 100) * (self.price * bought)
                bought_items = self.price * bought
                return bought_items - discount
            elif bought > 100:
                discount = (20 / 100) * (self.price * bought)
                return (self.price * bought) - discount

        def make_purchase(self, bought):

            self.amount -= bought

        def __str__(self):
            return 'Product name: {}; Amount: {}; Price: {}'.format(self.name, self.amount, self.price)
        

    
    product = Product('apples', 100, 6.99)
    print(f'{product}\n')
    print(f'total comes to {product.get_price(10):.2f}\n')
    product.make_purchase(10)
    print(f'{product}\n')
    

    n(2)


name()
