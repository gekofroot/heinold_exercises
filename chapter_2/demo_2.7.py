# Chapter 2
# 2.5 Exercises
# 7.

def n(x=0):
    print("\n" * x)


def main():
    
    n(1)

    sentence = ''
    for x in range(11):
        sentence += 'A'
    for x in range(8):
        sentence += 'B'
    for x in range(5):
        sentence += 'CD'
    sentence += 'E'
    for x in range(6):
        sentence += 'F'
    sentence += 'G'

    print(f'sentence: {sentence}')

    n(2)

main()
