from playingcards import *
from other import *
from input_validation import *
import random


class Round:
    def __init__(self, player, dealer, deck):
        self.player = player
        self.dealer = dealer
        self.deck = deck
        self.ante = 30

    def buy_in(self):
        self.player.chips = self.player.chips - self.ante

    def pay_out(self):
        self.player.chips = self.player.chips + (self.ante * 2)


    def round_start(self):
        self.buy_in()
        self.player.count_chips()
        self.player.deal(self.deck)
        self.dealer.draw(self.deck)
        self.player.reveal()
        self.dealer.reveal()
        self.player.print_hand_value()
        self.dealer.print_hand_value()

    def play_round(self):
        while self.player.bust is False and self.dealer.bust is False:
            self.round_start()

            while self.player.hand_value() < 21:
                if not self.player.hit_stay(self.deck):
                    break
                self.player.reveal()
                self.player.print_hand_value()

            if self.player.hand_value() > 21:
                print("{} is over 21, BUST!".format(self.player.name))
                self.player.bust = True

            print("Now dealer goes")
            while self.dealer.hand_value() < 17 and bust is False:
                self.dealer.draw(self.deck)
                self.dealer.reveal()
                if self.dealer.hand_value() > 21:
                    print("Dealer is over 21, BUST!")
                    bust = True
                    break

            print("End of round")
            if not bust:
                self.dealer.print_hand_value()
                self.player.print_hand_value()

                if self.dealer.hand_value() >= self.player.hand_value():
                    print("Dealer Wins!")
                else:
                    print("{} Wins {}!".format(self.player.name, self.ante))
                    self.pay_out()
                bust = True

    def clear_round(self):
        self.deck.reshuffle_hands(self.player, self.dealer)



def game_start():
    name = "Todd"  # input("Welcome to the table. What is your name: ")
    print("Ok " + Color.BOLD + name + Color.END + ", lets play blackjack!")

    dealer = Player("Dealer")
    player = Player(name)
    deck = Deck()
    random.shuffle(deck.cards)
    keep_playing = True

    while keep_playing:
        current_round = Round(player, dealer, deck)
        current_round.play_round()
        current_round.clear_round()
        if player.chips < current_round.ante:
            print("{} is out of chips. /sad trombone".format(player.name))
            keep_playing = False


game_start()
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