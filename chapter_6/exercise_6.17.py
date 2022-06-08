# Chapter 6
# 6.11 Exercises
# 17.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    let = "abcdefghijklmnopqrstuvwxyz"
    let_shft = []
    let_arg = ""
    for x in let:
        let_shft.append(x)

    count = 0
    print(let)
    for x in range(25):

        let_shft.append(let_shft[count])
        let_shft.remove(let_shft[count])

        for x in let_shft:
            let_arg += x
        print(let_arg)
        let_arg = ""

    n(2)


name()
