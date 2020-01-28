#hello world
#Blackjack
#todo create deck of cards- get creation from Hanabi Code
#ad graphic user interface

class card:
    def __init__(self, suit, number):
        self.s = suit #suite
        self.n = number #number

    def show(self):
        print("{} of {}".format(self.n, self.s))

class player:
    def __init__(self):
        pass

class deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades"]
card = card("Clubs", "Ace")
card.show()