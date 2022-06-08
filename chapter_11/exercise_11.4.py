# Chapter 11
# 11.5 Exercises
# 4.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    # global user_accounts
    user_accounts = {
        "username 1": "password a",
        "username 2": "password b",
        "username 3": "password c",
        "username 4": "password d",
        "username 5": "password e",
        "username 6": "password f",
        "username 7": "password g",
        "username 8": "password h",
        "username 9": "password i",
        "username 10": "password j",
    }

    while True:

        def username():
            enter_username = input("username: ")
            enter_password = input("password: ")
            if enter_username not in user_accounts:
                print(f"{enter_username} is not a valid user")
                n()
                username()
            else:
                print("print: ", user_accounts[enter_username])
                if user_accounts[enter_username] != enter_password:
                    print(f"incorrect password")
                else:
                    print(f"access granted")

        username()

    n(2)


name()
