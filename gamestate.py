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
        self.winner = False

    def buy_in(self):
        self.player.chips = self.player.chips - self.ante
        print("Ante up! {} pays {} chips.".format(self.player.name, self.ante))

    def pay_out(self):
        self.player.chips = self.player.chips + (self.ante * 2)
        print("Pay out! {} wins {} chips.".format(self.player.name, self.ante))

    def round_start(self):
        self.player.count_chips()
        self.buy_in()
        self.player.count_chips()
        self.player.deal(self.deck)
        self.dealer.draw(self.deck)
        self.player.reveal()
        self.dealer.reveal()
        self.player.hand_value = self.player.calc_hand_value()
        self.dealer.hand_value = self.dealer.calc_hand_value()
        self.player.print_hand_value()
        self.dealer.print_hand_value()

    def check_for_bust(self):
        player = self.player
        ace = False

        if player.hand_value > 21:
            for card in player.cards:
                if card.n == 1:
                    ace = True
        if ace is True:
            player.hand_value = player.hand_value - 10

        if player.hand_value > 21:
            return True
        else:
            return False

    def play_round(self):
        player_turn = True
        while not self.winner:
            self.round_start()

            while player_turn is True:
                player_turn = self.player.hit_stay(self.deck)
                self.player.reveal()
                self.player.print_hand_value()
                if self.check_for_bust() is True:
                    print("Player is over 21, BUST!")
                    self.player.bust = True
                    self.winner = self.dealer.name
                    player_turn = False

            if self.player.bust is True:
                print("Dealer wins!")
            else:
                print("Now dealer goes")

                while self.dealer.hand_value < 17:
                    self.dealer.draw(self.deck)
                    self.dealer.reveal()
                    if self.dealer.hand_value > 21:
                        print("Dealer is over 21, BUST!")
                        self.dealer.bust = True


            print("End of round")

            if self.dealer.bust:
                print("{} Wins !".format(self.player.name))
                self.pay_out()

            if not self.player.bust and not self.dealer.bust:
                self.dealer.print_hand_value()
                self.player.print_hand_value()

                if self.dealer.hand_value() >= self.player.hand_value():
                    print("Dealer Wins!")
                else:
                    print("{} Wins {}!".format(self.player.name, self.ante))
                    self.pay_out()

    def clear_round(self): # This function puts the playing cards into the discard, and resets the round
        self.deck.reshuffle_hands(self.player, self.dealer)
        self.player.ace = False
        self.player.bust = False
        self.dealer.ace = False
        self.dealer.bust = False



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