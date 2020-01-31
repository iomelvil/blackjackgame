from playingcards import Card
from playingcards import Deck
import random

class Player:
    def __init__(self, name):
        #self.hand = hand[]
        self.name = name

deck = Deck()
deck.show()
random.shuffle(deck.cards)
print("now shuffled\n")
deck.show()
print(deck.cards[2].s)
print("{} of {}".format(deck.cards[51].s, deck.cards[51].n))
print ("some bullshit")
deck.cards[51].show()

def gameloop
    while playstate = 1:
        #do game

#adding some bullshit