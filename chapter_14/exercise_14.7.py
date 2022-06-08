# Chapter 14
# 14.6 Exercises
# 7.

import random


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)



def name():
    n(1)

    class Card:
        
        def __init__(self, value, suit):
            self.value = value
            self.suit = suit

        def __str__(self):
            names = ['Jack', 'King', 'Queen', 'Ace']
            if self.value <= 10:
                return '{} of {}'.format(self.value, self.suit)
            else:
                return '{} of {}'.format(names[self.value-11], self.suit)


    class CardGroup:

        def __init__(self, cards=[]):
            self.cards = cards

        def next_card(self):
            return self.cards.pop(0)

        def has_card(self):
            return len(self.cards) > 0

        def size(self):
            return len(self.cards)

        def shuffle(self):
            random.shuffle(self.cards)

    class StandardDeck(CardGroup):

        def __init__(self):
            self.cards = []
            for s in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
                for v in range(2, 15):
                    self.cards.append(Card(v, s))


    def war():
        
        deck = StandardDeck()
        deck.shuffle()
        print(deck.size())

    war()



    n(2)


name()
