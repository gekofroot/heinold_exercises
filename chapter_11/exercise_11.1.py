# Chapter 11
# 11.5 Exercises
# 1.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    products = {}
    print(products)

    n()

    product_count = eval(input("amount of products: "))

    count = 1
    for x in range(product_count):
        print(f"product number: {count}\n")
        product_name = input("please input product_name: ")
        if product_name == "q":
            break
        else:
            product_price = eval(input("please input product_price: "))
            products[product_name] = product_price
            count += 1

    while True:
        product_query = input("product query: ")
        if product_query == "q":
            break
        elif product_query in products:
            print(f"{product_query}: ${products[product_query]}")
        else:
            if product_query[-1] == "s":
                print(f"{product_query} are not currently available at this time")
            else:
                print(f"{product_query} is not currently available at this time")

    while True:
        dollar_amount = eval(input("please enter dollar amount: "))
        for product, value in products.items():
            if value < dollar_amount:
                print(f"{product}: {value}")

    n()
    print(products)

    n(2)


name()
