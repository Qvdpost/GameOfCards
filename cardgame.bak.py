from random import shuffle

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ['Hearts','Diamonds','Clubs','Spades']
        self.values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

        self.cards = self.intialise_cards()

    def initialise_cards(self):
        return [Card(suit, value) for suit in self.suits
                for value in self.values]

    def __str__(self):
        """
        This method allows us to specify how a deck object should
        be printed in the terminal.
        """

        return "Cards remaining in deck: {}".format(len(self.cards))

    def shuffle(self):
        """ This method shuffles the deck and then returns something. """
        # TODO: Implement the shuffling algorithm.
        if len(self.cards) < 1:
            raise ValueError("No cards left in the deck.")
        shuffle(self.cards)


    def deal(self):
        """
        This method takes the top card from the deck and returns it.
        If no more cards are present, an error is raised instead.
        """
        if len(self.cards) == 0:
            raise ValueError("All cards have been dealt")

        return self.cards.pop()

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    print("Dealt cards: ")
    for _ in range(5):
        card = deck.deal()
        print(card)
    print("The Deck: ")
    for card in deck.cards:
        print(card)
