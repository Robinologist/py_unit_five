import random

# Global variables
deck = []  # a list representing the deck of cards

# Helper function to initialize the deck of cards
def initialize_deck():
  global deck
  suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
  ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
  for suit in suits:
    for rank in ranks:
      deck.append((suit, rank))

# Helper function to shuffle the deck of cards
def shuffle_deck():
  global deck
  random.shuffle(deck)

# Initialize the deck of cards
initialize_deck()

# Shuffle the deck of cards
shuffle_deck()

# Print the deck of cards
print('Deck of cards:')
for card in deck:
  suit, rank = card
  print(f'{rank} of {suit}')