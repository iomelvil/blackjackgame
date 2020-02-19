from enum import Enum
from random import randint

class CardValue(Enum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13


class CardSuit(Enum):
    Club = 1
    Heart = 2
    Diamond = 3
    Spade = 4


class Card(tuple):
    def __new__(cls, value, suit):
        assert isinstance(value, CardValue)
        assert isinstance(suit, CardSuit)
        return tuple.__new__(cls, (value, suit))

    def __setattr__(self, *ignored):
        raise NotImplementedError

    def __delattr__(self, *ignored):
        raise NotImplementedError

    def __str__(self):  # Prints card displaying suit and number as text
        return "{} of {}s".format(self.value.name, self.suit.name)

    @property
    def value(self): # print(card.value) shows card # only (ace -> king) suit can be ignored for blackjack logic for now
        return self[0]

    @property
    def suit(self):
        return self[1]


class Deck:
    def __init__(self):
        self.cards  = [Card(value, suit) for value in CardValue for suit in CardSuit]
        self.size = len(self.cards)

    def show(self):
        for card in self.cards:
            print(card)

    def __str__(self):
        return  str(self.size) + " cards |" + " " + (', '.join(str(card) for card in self.cards))


class Player:
    def __init__(self, name):
        self.cards = []
        self.name = name
        self.chips = 100

    def __str__(self):
        return "{} has {} chips. Current Hand: {}".format(self.name, self.chips, (', '.join(str(card) for card in self.cards)))

    def draw(self, deck, count): # Randomly draws a card from the deck and places it in players hand
        for i in range(count):
            self.cards.append(deck.cards.pop(randint(0, deck.size - 1)))
            deck.size -= 1

class Round:
    def __init__(self):
        self.ante = 10
        self.pot = 0
        self.winner = "none"

    def payout(self): pass


deck = Deck()
player = Player("Bob")
print(deck)
print(deck.size)
print("\n")
player.draw(deck, 3)
print(player)
print(deck)
# adding comment ss