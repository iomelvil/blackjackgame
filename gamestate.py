from playingcards import *
from other import *
from input_validation import *

def game_start():
    name = "Todd" #input("Welcome to the table. What is your name: ")
    print("Ok " + Color.BOLD + name + Color.END + ", lets play blackjack!")

    dealer = Player("Dealer")
    player = Player(name)
    keep_playing = True
    deck = Deck()
    random.shuffle(deck.cards)

    while keep_playing:
        player.deal(deck)
        dealer.draw(deck)
        player.reveal()
        dealer.reveal()
        player.print_hand_value()
        dealer.print_hand_value()

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
        dealer.reveal()
        while dealer.hand_value() < 17:
            dealer.draw(deck)
        if dealer.hand_value() > 21:
            print("Dealer is over 21, BUST!")
        print("now dealer goes")

game_start()