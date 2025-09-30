class Card:
    def __init__(self, value, suit):
        self.value = value
        self.color = suit

suits = ['Diamonds','Clubs','Hearts','Spades']
values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']


deck = [Card(value, suit) for value in values for suit in suits]