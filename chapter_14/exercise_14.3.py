# Chapter 14
# 14.6 Exercises
# 3.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)



def name():
    n(1)

    class PasswordManager:

        def __init__(self):
                self.old_passwords = []
                for s in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
                    self.old_passwords.append(s)

        def get_password(self):
            return self.old_passwords[-1]

        def set_password(self):
            new_password = input("new password: ")
            if new_password == self.old_passwords[-1]:
                while new_password == self.old_passwords[-1]:
                    print("cannot set new password to current password, please enter a new password... ")
                    new_password = input("new password: ")

            self.old_passwords.append(new_password)

        def is_correct(self, string):
            if string == self.old_passwords[-1]:
                print(True)
            elif string != self.old_passwords[-1]:
                print(False)
        
        def __str__(self):
            return 'old passwords:{}'.format(self.old_passwords)
    
    passwordmanager = PasswordManager()#PasswordManager(passwords)
    print(f'current password: {passwordmanager.get_password()}')
    passwordmanager.set_password()
    print(f'current password: {passwordmanager.get_password()}')
    check_string = input("check string: ")
    passwordmanager.is_correct(check_string)


    n(2)


name()
