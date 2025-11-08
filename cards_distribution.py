import random
from cards import Card

# num_of_players = int(input('Enter number of players:'))
class Distribution:

    def __init__(self):
        self.cards = Card()
        self.deck_of_cards = self.cards.deck_creation()
        print(self.deck_of_cards)
        self.burnt_cards = list()

    def dealing(self):
        card = random.choice(deck_of_cards)
        deck_of_cards = self.deck_of_cards.pop(card)
        self.burnt_cards.append(card)
        return card
    
    





