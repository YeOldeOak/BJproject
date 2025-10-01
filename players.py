import deck

class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.cards = [deck.Card]

    def __repr__(self):
        return f"Balance of {self.name}: {self.balance}, current cards: {self.cards}"
    