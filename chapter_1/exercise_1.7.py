# Chapter 1
# 1.8 Exerceises
# 7.

from os import system


def n(x=0):
    print("\n" * x)

def t(x=7):
    t = '\t' * x
    return t

def main():
    
    n(1)
    
    # initialize screen
    def initialize_screen():
        
        system('clear')
        n(14)
    
    # message for invalid entry
    def invalid_entry():
        
        input(f'\n{t()}invalid entry... press return ')
    
    #convert weight from kilograms to pounds / pounds to kilograms
    def convert_weight(unit_a, unit_b, operator):
        
        initialize_screen()
        
        while True:
            try:
                weight = eval(input(f'{t()}enter weight in {unit_a}: '))
                break
            except (ValueError, TypeError, NameError, SyntaxError):
                invalid_entry()
                initialize_screen()
        
        # operator selected based on arg
        if operator == "/":
            convert_weight = weight / 2.2
        elif operator == "*":
            convert_weight = weight * 2.2

        print(f'\n{t()}{weight:.2f} {unit_a} is equal to {convert_weight:.2f} {unit_b}')
        input(f'\n{t()}press return... ')
    
    # display options menu
    def menu():
        
        options = ["convert to pounds", "convert to kilograms", "exit"]
        
        while True:
            initialize_screen()
            
            while True:
                try:
                    count = 1
                    for option in options:
                        print(f'{t()}{count}. {option}')
                        count += 1
                    n()
                    selection = eval(input(f'{t()}selection: '))
                    break
                except (ValueError, TypeError, NameError, SyntaxError):
                    invalid_entry()
                    initialize_screen()

            if selection == 1:
                # convert weight from kilograms to pounds
                convert_weight('kilograms', 'pounds', '/')
            elif selection == 2:
                # convert weight from pounds to kilograms
                convert_weight('pounds', 'kilograms', '*')
            elif selection == 3:
                system('clear')
                break
            else:
                invalid_entry()
    
    menu()


    n(2)


main()
