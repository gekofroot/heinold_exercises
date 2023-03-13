# Chapter 6
# 6.11 Exercises
# 23cd.

def n(x=0):
    print("\n" * x)

n(1)

print("message encryption")

message = input("enter message: ")

print(f"message: {message}")

integer = eval(input("enter an integer: "))

encrypted_message = ""

count = 0
for x in range(integer):
    for x in range(len(message)):
        if x % integer == count:
            encrypted_message += message[x]
    count += 1

print(f"encrypted message: {encrypted_message}")

print("\n\n\n")

print("message decryption")

decrypted_message = ""

for x in range(len(encrypted_message)):
    for y in range(integer):
        if x % integer == y:
            decrypted_message += message[x]

print(f"decrypted_message: {decrypted_message}")

n(2)
