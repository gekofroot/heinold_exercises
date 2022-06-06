# Chapter 1
# 1.8 Exercises
# 6.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)
    
    number = eval(input("enter a number: "))
    nummul = []

    count = 1
    for x in range(5):
        x_times = number * count
        nummul.append(str(x_times))
        count += 1
    
    nummul = '---'.join(nummul)
    print(nummul)

    n(2)

main()
