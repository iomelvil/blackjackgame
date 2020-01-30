from playingcards import *
from other import *

name = input("Welcome to the table. What is your name: ")
print("Ok " + Color.BOLD + name + Color.END + ", lets play blackjack!")

player1 = Player(name)
player2 = Player("Houes")

deck = Deck()
random.shuffle(deck.cards)
deck.show()
print("\n")
deck.cards[0].show()
print("\n")

player1.draw(deck)
player1.show()
print("\n")
deck.cards[0].show()
print("\n")
deck.show()
#while True: