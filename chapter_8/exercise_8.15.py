# Chapter 8
# 8.7 Exercises
# 15.

def n(x=0):
    print("\n" * x)

n(1)

element = [[[1], [0] * x] for x in range(12) for y in range(x - x + 1)]
element = [x for y in element for x in y]
element = [x for y in element for x in y]
element.append(1)
print(f"\nelement: {element}")

n(2)
