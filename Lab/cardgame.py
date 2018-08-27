from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def display_card(self):
        print(f"{self.value} of {self.suit}")

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ['Hearts','Diamonds','Clubs','Spades']
        self.values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

        # TODO: Create a deck of cards.
        self.cards = self.intialize_cards()

    def initialize_cards(self):
        return [Card(suit, value) for suit in self.suits
                for value in self.values]

    def __str__(self):
        """
        This method allows us to specify how a deck object should
        be printed in the terminal.
        """
        # TODO: Implement the correct string to be printed.
        # NOTE: Do we provide this?
        return "Cards remaining in deck: {}".format(len(self.cards))

    def shuffle(self):
        """ This method shuffles the deck and then returns something. """
        # TODO: Implement the shuffling algorithm.
        if len(self.cards) < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)

        # NOTE: Return something, but what?
        # return self

    def deal(self):
        """
        This method takes the top card from the deck and returns it.
        If no more cards are present, an error is raised instead.
        """
        if len(self.cards) == 0:
            raise ValueError("All cards have been dealt")
        # TODO: Implement the dealing of a card.
        return self.cards.pop()
