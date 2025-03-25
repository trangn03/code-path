"""
Step 1: Copy the following code into your IDE.

Step 2: Instantiate an instance of the class Player and store it in a variable named player_one.

The Player object should have the character "Yoshi" and the kart "Super Blooper". 
"""

class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
        
# Example Usage:

player_one.character
player_one.kart
player_one.items

"""
Example Output:

Yoshi
Super Blooper
[]
"""