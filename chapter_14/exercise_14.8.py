# Chapter 14
# 14.6 Exercises
# 8.

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
            return random.shuffle(self.cards)
        
        def next2(self):
            top_two_cards = []
            top_two_cards.append(self.cards.pop(0))
            top_two_cards.append(self.cards.pop(0))
            return top_two_cards

    class HalfDeck(CardGroup):
        
        def __init__(self):
            self.cards = []
            for s in ['Hearts', 'Spades']:
                for v in range(2, 10):
                    self.cards.append(Card(v, s))

        #def next2(self):
        #    top_two_cards = []
        #    top_two_cards.append(self.cards.pop(0))
        #    top_two_cards.append(self.cards.pop(0))
        #    return top_two_cards


    deck = HalfDeck()

    print(f'top two cards from half deck: {deck.next2()}')
    print(f'top card from half deck: {deck.next_card()}')
        





    n(2)


name()
