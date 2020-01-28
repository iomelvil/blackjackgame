#hello world
#Blackjack
#todo add shuffle deck method from hanabi code and draw card
import random

class Card:
    def __init__(self, suit, number):
        self.s = suit #suite
        self.n = number #number

    def show(self):
        if self.n == 1:
            print("{} of {}".format("Ace", self.s))
        if self.n < 11 and self.n > 1:
            print("{} of {}".format(self.n, self.s))
        if self.n == 11:
            print("{} of {}".format("Jack", self.s))
        if self.n == 12:
            print("{} of {}".format("Queen", self.s))
        if self.n == 13:
            print("{} of {}".format("King", self.s))

class Player:
    def __init__(self, name):
        self.hand = hand[]
        self.name = name

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for n in range(1, 14):
                self.cards.append(Card(s, n))

    def show(self):
        for card in self.cards:
            card.show()

deck = Deck()
deck.show()



