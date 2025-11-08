class Card:
   def __init__(self):
      ''' It initializes card numbers and shapes '''
      self.numbers = ['A','k','Q','J','10','9','8','7','6','5','4','3','2'] # class variables
      self.shapes = ['spades','diamond','hearts','clubs']
   
   def deck_creation(self):
      '''Create of deck of poker cards for game'''
      deck_of_cards = list()
      for shape in self.shapes:
         for num in self.numbers:
            deck_of_cards.append(shape+num)
      return deck_of_cards