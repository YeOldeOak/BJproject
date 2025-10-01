class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"
    
    def __iter__(self):
        return iter((self.value, self.suit))

suits = ['Diamonds','Clubs','Hearts','Spades']
values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']


card_deck = [Card(value, suit) for value in values for suit in suits]
