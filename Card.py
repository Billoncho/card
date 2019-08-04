# Card.py
# Billy Ridgeway
# Generates a playing card.

import random   # Imports the random library.

# Creates a list of suits.
suits = ["clubs", "diamonds", "hearts", "spades"]

# Creates a list of the card faces.
faces = ["two", "three", "four", "five", "six",
         "seven", "eight", "nine", "ten", "jack",
         "queen", "king", "ace"]

my_face = random.choice(faces)  # Chooses a random card face.
my_suit = random.choice(suits)  # Chooses a random card suit.

# Prints the player's card to the screen.
print("I have the", my_face, "of", my_suit, ".")

    
    
