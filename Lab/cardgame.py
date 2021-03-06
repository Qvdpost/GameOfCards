from random import shuffle

class Card(object):
    """
    Representation of a single playing card.
    """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck(object):
    """
    Representation of a full deck of 52 playing cards.
    """
    def __init__(self):
        print("Creating a Deck object.")
        self.suits = ['Hearts','Diamonds','Clubs','Spades']
        self.values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

        self.cards = [] # TODO: Initialize the list of cards.

if __name__ == "__main__":
    pass
