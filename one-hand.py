import deck
import random
import players
import dealer

simple_deck = deck.card_deck
test_players = [players.Player("Jack", 500), players.Player("Bob", 500)]
test_dealer = dealer.Dealer((),())

print(f"starting deck length = {len(simple_deck)}")


def play_hand(deck, players):
    deck_length = len(deck)
    discard_pile = []
    nr_players = len(players)

    # Drawing phase

    # First card for each player
    for i in range(nr_players):
        temp_rand = random.randint(0, (len(deck)-1))
        drawn_card = deck[temp_rand]

        players[i].cards.extend(drawn_card)
        discard_pile.extend(drawn_card)
        del deck[temp_rand]
        deck_length = deck_length - 1

    # First card for dealer   
    dealer_rand = random.randint(0, (len(deck)-1))
    dealer_drawn_card = deck[dealer_rand]

    test_dealer.face_card = dealer_drawn_card
    discard_pile.extend(dealer_drawn_card)
    del deck[dealer_rand]
    deck_length = deck_length - 1

    # Second card for each player
    for j in range(nr_players):
        temp_rand = random.randint(0, (len(deck)-1))
        drawn_card = deck[temp_rand]

        players[j].cards.extend(drawn_card)
        discard_pile.extend(drawn_card)
        del deck[temp_rand]
        deck_length = deck_length - 1


    # Second card for dealer    
    dealer_second_rand = random.randint(0, (len(deck)-1))
    dealer_second_drawn_card = deck[dealer_second_rand]

    test_dealer.hidden_card = dealer_second_drawn_card
    discard_pile.extend(dealer_second_drawn_card)
    del deck[dealer_second_rand]
    deck_length = deck_length - 1
        
    print(test_dealer)
    print(f"deck length now: {deck_length}")
    print(players[0])
    print(players[1])
        
play_hand(simple_deck, test_players)
