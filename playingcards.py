#hello world
#Blackjack
#todo enum the card deck suits
#todo figure out how to deal with aces being 11 OR 1
#lock hit prompt only accept y or no
import random
from input_validation import yes_or_no

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

    def value(self):
        if self.n > 9:
            return 10
        else:
            return self.n


class Player:
    def __init__(self, name):
        self.cards = []
        self.name = name

    def draw(self,deck):
        deck.cards[0].show()
        self.cards.append(deck.cards.pop(0))

    def deal(self,deck):
        self.cards.append(deck.cards.pop(0))
        self.cards.append(deck.cards.pop(0))

    def show(self):
        print("\n{}'s hand:".format(self.name))
        self.cards[0].show()

    def reveal(self):
        print("\n{}'s hand:".format(self.name))
        for card in self.cards:
            card.show()

    def hand_value(self):
        sum = 0
        for card in self.cards:
           sum = sum + card.value()
        return sum

    def print_hand_value(self):
        sum = 0
        for card in self.cards:
            sum = sum + card.value()
        print("\n{}'s hand value is: {}".format(self.name, sum))
        return sum

    def hit_stay(self, deck,):
        hit = yes_or_no("Would you like to hit?")
        if hit:
            self.draw(deck)
        else:
            print("{} will stay at {}".format(self.name, self.hand_value()))
        return hit

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




