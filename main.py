import deck
import random

# Shuffles the deck inputted to function
def shuffle_up(decks):
    random.shuffle(decks)

    return decks

# Stacks amount_of_decks amount of 52 card decks into one big deck
def make_decks(amount_of_decks):
    single_deck = deck.card_deck
    print(amount_of_decks)
    big_deck = single_deck * amount_of_decks
           
    return big_deck



