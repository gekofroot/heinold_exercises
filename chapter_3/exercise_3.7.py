# Chapter 3
# 3.8 Exercises
# 7.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    angle = eval(input(f'enter an angle between -180 and 180 degrees: '))
    
    convert_angle = (angle % 360) + 180

    print(f'angle converted: {convert_angle}')

    n(2)

main()
