from enum import Enum
from random import randint
from input_validation import yes_or_no


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
    def value(self):  # print(card.value) shows card # only (ace -> king) suit can be ignored for blackjack logic
        return self[0]

    @property
    def suit(self):
        return self[1]


class Deck:
    def __init__(self):
        self.cards = [Card(value, suit) for value in CardValue for suit in CardSuit]
        self.size = len(self.cards)

    def show(self):
        for card in self.cards:
            print(card)

    def __str__(self):
        return str(self.size) + " cards |" + " " + (', '.join(str(card) for card in self.cards))


class Player:
    def __init__(self, name, chips=100):  # TODO Could add player.hand_value as an attribute instead of recalc each time
        self.cards = []
        self.name = name
        self.chips = chips

    def __str__(self):
        return "{} has {} chips. Current Hand: {}".format(self.name, self.chips, (', '.join(str(card) for card in self.cards)))

    # Draws a card from the deck into the players hand. If a seed between 1-52 is requested,
    # one specific card in the deck is drawn.
    def draw(self, deck, count=1, seed=0):
        if 0 < seed <= deck.size:
            self.cards.append(deck.cards.pop(seed-1))
            deck.size -= 1
        else:
            for i in range(count):
                self.cards.append(deck.cards.pop(randint(0, deck.size - 1)))
                deck.size -= 1

    # Asks for a bet less than your chip count.
    def place_bet(self):
        while "the answer is invalid":
            reply = int(input("How much will you bet? You have " + str(self.chips)))
            if 0 < reply <= self.chips:
                return reply

    def discard(self):
        self.cards = []

    def show(self):
        print("{} has:".format(self.name), end=" ")
        for card in self.cards:
            print(card, end=", ")
        print("\n")

    # Calculates the hand value, assumes Aces are 11s unless over 21.
    def hand_value(self):
        hand_sum = 0
        ace_count = 0
        for card in self.cards:
            if card.value.value == 1:
                ace_count += 1
                hand_sum += 11
            elif card.value.value <= 10:
                hand_sum += card.value.value
            else:
                hand_sum += 10
        while ace_count > 0:
            if hand_sum > 21:
                hand_sum -= 10
            ace_count -= 1
        return hand_sum

    def check_blackjack(self):
        if len(self.cards) == 2 and self.hand_value() == 21:
            return True
        else:
            return False

    def hit_stay(self, deck):
        hit = yes_or_no("Would you like to hit?")
        if hit:
            self.draw(deck, 1)
        else:
            print("{} will stay at {}".format(self.name, self.hand_value()))
        return hit

    def bot_hit_stay(self, deck):
        while self.hand_value() < 17:
            self.draw(deck, 1)
            self.show()
            if self.hand_value() > 21:
                print("Bust!!!")
                return self.hand_value()
        if self.hand_value() >= 17:
            print("{} will stay at {}".format(self.name, self.hand_value()))


class Round:
    def __init__(self, player, dealer, deck):
        self.pot = 0
        self.player = player
        self.dealer = dealer
        self.deck = deck

    def round_bet(self):
        bet = self.player.place_bet()
        self.pot += bet
        self.player.chips -= bet

    def pay_out(self, winner):
        winner.chips += self.pot * 2
        print("Payout {} to {}".format(self.pot, winner.name))
        self.pot = 0

    def print_winner(self, winner):
        print("{} wins!".format(winner.name))

    def determine_winner(self, player, dealer):
        player_hand_value = player.hand_value()
        dealer_hand_value = dealer.hand_value()
        if player_hand_value <= 21 and dealer_hand_value <= 21:
            if player_hand_value == dealer_hand_value:
                print("push")
                return dealer
            else:
                if player_hand_value > dealer_hand_value:
                    return player
                else:
                    return dealer





def game_start():
    deck = Deck()
    player = Player("Bob")
    dealer = Player("Dealer", 9999)
    game_over = False

    # print(deck)
    # player.draw(deck, 1, 1)
    # player.draw(deck, 1, 51)
    # print(player)
    # print(player.hand_value())
    # print(player.check_blackjack())
    round_count = 1
    while not game_over:
        print("Round {}".format(round_count))
        round = Round(player, dealer, deck)
        round.round_bet()
        initial_draw(player, dealer, deck)
        check_blackjack(round, player, dealer)

        while player.hand_value() <= 21:
            if player.hit_stay(deck):
                player.show()
                print(player.hand_value())
            else:
                break

        dealer.bot_hit_stay(deck)
        winner = round.determine_winner(player, dealer)
        print("{} wins!".format(winner.name))
        round.pay_out(winner)
        player.discard()
        dealer.discard()
        round_count += 1  # indicates round end


def initial_draw(player, dealer, deck):  # to set player to have blackjack, draw with seeds 1 and 51
    player.draw(deck, 1)
    dealer.draw(deck, 1)
    player.draw(deck, 1)
    print(player)
    dealer.show()
    dealer.draw(deck, 1)


def check_blackjack(round, player, dealer):
    if player.check_blackjack() or dealer.check_blackjack():
        if player.check_blackjack() and dealer.check_blackjack():
            print("Ya both got blackjack. Dealer is forgiving")
            round.pay_out(player)
        if player.check_blackjack():
            print("Blackjack!")
            round.print_winner(player)
            round.pay_out(player)
        if dealer.check_blackjack():
            print("Blackjack!")
            round.print_winner(dealer)
            round.pay_out(player)





game_start()