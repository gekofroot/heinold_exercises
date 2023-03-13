# Chapter 6
# 6.11 Exercises
# 23ab.

def n(x=0):
    print("\n" * x)

n(1)

print("message encryption")

message = input("enter a message: ")

print(f"message: {message}")

encrypted_message = ""

for y in range(3):
    for x in range(len(message)):
        if x % 3 == y:
            encrypted_message += message[x]
        
print(f"encrypted message: {encrypted_message}")

print("\n\n\n")

print("message decryption")

decrypted_message = ""

for x in range(len(encrypted_message)):
    for y in range(3):
        if x % 3 == y:
            decrypted_message += message[x]

print(f"\ndecrypted message: {decrypted_message}")

n(2)
