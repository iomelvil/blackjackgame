from playingcards import *
from other import *
from input_validation import *
import random


class Round:
    def __init__(self, deck, player, dealer):
        self.pot = pot
        self.winner = winner
        self.deck = deck
        self.discard = discard
        self.player = player
        self.dealer = dealer

    def round_start(self):
        self.player.deal(deck)
        self.dealer.draw(deck)
        self.player.reveal()
        self.dealer.reveal()
        self.player.print_hand_value()
        self.dealer.print_hand_value()



def game_start():
    name = "Todd" # input("Welcome to the table. What is your name: ")
    print("Ok " + Color.BOLD + name + Color.END + ", lets play blackjack!")

    dealer = Player("Dealer")
    player = Player(name)
    keep_playing = True
    deck = Deck()
    random.shuffle(deck.cards)

    while keep_playing:
        round = Round(deck, player, dealer)
        round.round_start()


        while player.hand_value() <= 21:
            if not player.hit_stay(deck):
                break
            player.reveal()
            player.print_hand_value()

        if player.hand_value() > 21:
            print("{} is over 21, BUST!".format(player.name))
            keep_playing = yes_or_no("Would you like to keep playing?")
            if keep_playing:
                deck.reshuffle_hands(player, dealer)
        dealer.reveal() # this still shows dealer has 4 cards? -- loop structure isnt right, dealer is going after ershuffle
        while dealer.hand_value() < 17:
            dealer.draw(deck)
        if dealer.hand_value() > 21:
            print("Dealer is over 21, BUST!")
        print("now dealer goes")

"""
 while keep_playing:
    ask for ante (if no, don't keep playing)
    while round--round as class has attr: pot, players, winner, deck
        print current $
        reshuffle() reshuffle if necessary
        deal()
        player goes()
        dealer goes()
        assign winner and payout()
            winner()
            payout()
        hands to discard        
 if 
 
 
 """




game_start()