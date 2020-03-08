from enum import Enum
from random import randint


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
        self.cards  = [Card(value, suit) for value in CardValue for suit in CardSuit]
        self.size = len(self.cards)

    def show(self):
        for card in self.cards:
            print(card)

    def __str__(self):
        return  str(self.size) + " cards |" + " " + (', '.join(str(card) for card in self.cards))


class Player:
    def __init__(self, name):
        self.cards = []
        self.name = name
        self.chips = 100

    def __str__(self):
        return "{} has {} chips. Current Hand: {}".format(self.name, self.chips, (', '.join(str(card) for card in self.cards)))

    # Draws a card from the deck into the players hand. If a seed between 1-52 is requested,
    # one specific card in the deck is drawn.
    def draw(self, deck, count, seed=0):
        if 0 < seed <= deck.size:
            self.cards.append(deck.cards.pop(seed-1))
            deck.size -= 1
        else:
            for i in range(count):
                self.cards.append(deck.cards.pop(randint(0, deck.size - 1)))
                deck.size -= 1

    def place_bet(self, round):
        player_bet = input("How much will you bet?")
        self.chips -= player_bet
        round.pot += player_bet

    def discard(self):
        self.cards = []

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



class Round:
    def __init__(self, player, dealer, deck):
        self.pot = 0

    def pay_out(self, winner):
        pass


deck = Deck()
player = Player("Bob")
print(deck)
player.draw(deck, 1, 1)
player.draw(deck, 1, 1)
player.draw(deck, 1)
print(player)
print(player.hand_value())