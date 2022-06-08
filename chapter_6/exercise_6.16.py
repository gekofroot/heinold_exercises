# Chapter 6
# 6.11 Exercises
# 16.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    n(1)

    place = input("travel destination: ")
    noun = input("noun: ")
    sen = input("please enter name: ")
    item = input("special requests: ")
    clothing_type = input("favourite clothing type: ")
    clothing_brand = input("clothing brand: ")

    print(f'\n\nDear {sen}, \nWe welcome you to {place.title()} and we hope you enjoy your stay here at The {noun.title()} Inn and Suites. \nIn addition to the continental breakfast, swimming pool and jacuzzi, we have also provided your complimentary {item}. Please be advised that wearing {clothing_type} during your stay with us is highly discouraged, due to a partnership we have with {clothing_brand.title()}. Feel free to contact front reception with any questions comments or concerns.')

    n(2)


name()
