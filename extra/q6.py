# Q6
# Create a deck of cards class. Internally, the deck
# of cards should use another class, a card class.
# Your requirements are:
#
# The Deck class should have a deal method to deal
# a single card from the deck
# After a card is dealt, it is removed from the deck.
# There should be a shuffle method which rearranges
# them randomly. The Card class should
# have a suit (Hearts, Diamonds, Clubs, Spades)
# and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)

from random import shuffle

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return "{} {}".format(self.suit, self.value)

class Deck:

    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in list(range(2, 11)) + ['A', 'K', 'Q', 'J']:
                newCard = Card(suit, value)
                self.cards.append(newCard)

    def deal(self):
        return self.cards.pop()

    def shuffle(self):
        shuffle(self.cards)

deck = Deck()
deck.shuffle()
print(deck.deal())
