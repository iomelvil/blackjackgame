from playingcards import *
from other import *
from cardvalue import *



name = "Todd" #input("Welcome to the table. What is your name: ")
print("Ok " + Color.BOLD + name + Color.END + ", lets play blackjack!")

dealer = Player("Dealer")
player = Player(name)

deck = Deck()
random.shuffle(deck.cards)

player.deal(deck)
dealer.deal(deck)
player.reveal()
dealer.reveal()
player.hand_value()
dealer.hand_value()
player.hit_stay(deck)
player.hand_value()
#while True: