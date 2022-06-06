# Chapter 3
# 3.8 Exercises
# 9.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    # 12 and 0
    initial_hour = eval(input(f'enter hour: '))
    hours_ahead = eval(input(f'hours ahead? '))
    
    new_hour = (initial_hour + hours_ahead) % 12
    
    print(f'new hour: {new_hour}')

    n(2)

main()
