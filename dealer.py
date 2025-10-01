class Dealer:
    def __init__(self, face_card, hidden_card):
        self.face_card = face_card
        self.hidden_card = hidden_card
    
    # remove hidden card part if needed
    def __repr__(self):
        return f"Dealer is showing {self.face_card} (hidden card is: {self.hidden_card})"
