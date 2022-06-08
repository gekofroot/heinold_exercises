# Chapter 9
# 9.6 Exercises
# 14b.

from random import choice, randint
from os import system
from time import sleep
import sys


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def name():
    # n(1)

    global purse
    global progress_bar_str
    global progress_bar_lis

    #apres guess
    correct = ["...", "good job", "well in", "good guess", "correct", "solid guess"]    
    incorrect = ["incorrect", "thats not it...", "not it", "...", "good try.."]
    
    #coin choice
    coin = ["heads", "tails"]
    purse = 100
    
    # build/fill progress line
    progress_bar_str = ""
    progress_bar_lis = []
    for x in range(50):
        progress_bar_lis += "#"

    for x in progress_bar_lis:
        progress_bar_str += x

    progress_lin = ""
    for x in range(100):
        progress_lin += "_"

    win_collect = 9
    lose_remove = 10

    #bonus round switches
    bonus_round_played_a = 0
    bonus_round_played_b = 0
    bonus_round_played_c = 0
    bonus_round_played_d = 0
    bonus_round_played_e = 0
    t = "\t" * 8

    def current_progress():
        """print current progress and purse amount"""
        
        n(7)
        print(f'\t\t\t{progress_bar_str}')
        print(f'\t\t\t{progress_lin}\n\n\n')
        print(f'{t}[ purse: ${purse} ]\n\n')
        #a = f"\t\t\t{progress_bar_str}"
        #i = f"\t\t\t{progress_lin}\n\n\n"
        #x = f"{t}[ purse: ${purse} ]\n\n"
        #return x
    

    def bonus_round(name, add_bonus, remove_bonus, topint):
        """
        defines bonues round behaviours
        """
        
        global progress_bar_str
        global progress_bar_lis
        global purse
        current_progress()

        print(f'{t}{name}\n')
        print(f'{t}gain ${add_bonus} for a correct answer\n{t}lose ${remove_bonus} for an incorrect answer\n')
        num_a = randint(0, 10)
        num_b = randint(0, topint)
        test_question = print(f'{t}what is {num_a} x {num_b} ?')
        user_guess = input(f'{t}answer: ')
        answer = num_a * num_b
        # add bonus for correct answer
        if user_guess == str(answer):
            print(f'{t}correct')
            n()
            print(f'{t}adding $15 to purse')
            purse += add_bonus
            perfadd = (add_bonus / 200) * 100
            progress_bar_lis += "#" * int(perfadd)
        else:
            # remove bonus for incorrect answer
            print(f'{t}incorrect, answer to {num_a} x {num_b} is {num_a * num_b}')
            n()
            print(f'{t}removing $20 from purse')
            purse -= remove_bonus
            perfadd = (remove_bonus / 200) * 100
            progress_bar_lis = progress_bar_lis[: -int(perfadd)]
        
        # update progress bar
        progress_bar_str = ""
        for x in progress_bar_lis:
            progress_bar_str += x
        
        n()
        input(f'{t}press enter... ')
        system("clear")
        n(2)
    
    # play to
    top_num = 200
    
    while purse > 0 and purse <= top_num:
        
        # all bonus round attributes
        if 5 <= purse <= 10:
            if bonus_round_played_a < 3:
                bonus_round("bonus round A", 5, 4, 5)
                bonus_round_played_a += 1
        if 50 <= purse <= 60:
            if bonus_round_played_b < 3:
                bonus_round("bonus round B", 10, 15, 10)
                bonus_round_played_b += 1
        if 70 <= purse <= 90:
            if bonus_round_played_c < 2:
                bonus_round("bonus round C", 15, 20, 10)
                bonus_round_played_c += 1
        if 120 <= purse <= 150:
            if bonus_round_played_d < 2:
                bonus_round("bonus round D", 20, 50, 15)
                bonus_round_played_d += 1
        if 190 <= purse <= 199:
            if bonus_round_played_e < 1:
                bonus_round("bonus round E", 5, 100, 20)
                bonus_round_played_e += 1

        current_progress()
        
        def window():
            
            global coin_flip
            global progress_bar_str
            global progress_bar_lis
            global purse

            coin_flip = choice(coin)
            print(f'{t}  coin flip... \n')

            userguess = input(f"{t}heads or tails? ")
            if userguess == coin_flip:
                sleep(2)
                system("clear")
                n(2)
                current_progress()
                print(f'{t}coin flip result: {coin_flip}\n')
                print(f'{t}{choice(correct)}\n')
                print(f'{t}adding ${win_collect} to purse')
                purse += win_collect
                perfadd = (win_collect / top_num) * 100
                progress_bar_lis += "#" * int(perfadd)
            elif userguess != coin_flip:
                sleep(2)
                system("clear")
                n(2)
                current_progress()
                print(f'{t}coin flip result: {coin_flip}\n')
                print(f'{t}{choice(incorrect)}\n')
                print(f'{t}removing ${lose_remove} from purse')
                purse -= lose_remove
                perfadd = (lose_remove / top_num) * 100
                progress_bar_lis = progress_bar_lis[: -int(perfadd)]
            
            # update progress bar
            progress_bar_str = ""
            for x in progress_bar_lis:
                progress_bar_str += x
            n(2)
            input(f'{t}press enter... ')
            system("clear")
            n(2)
        window()

    # print final game statistics
    print(f'\t\t{progress_bar_str}')
    print(f'\t\t{progress_lin}\n\n')
    print("game over")
    print(f'you finished the game with ${purse} in your purse')


name()
