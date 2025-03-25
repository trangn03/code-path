"""
In the previous exercise, we accessed and modified a player’s kart attribute directly. Instead of allowing users to update their player directly, it is common to create setter methods that users can call to update class attributes. This has a few different benefits, including allowing us to validate data before updating our class instance.

Update your Player class with a method set_character() that takes in one parameter name.

If name is valid, it should update the player’s character attribute to have value name and print "Character updated".
Otherwise, it should print out "Invalid character".
Valid character names are "Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", and "Bowser". 
"""
class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
        
    def set_character(self, name):
        pass


# Example Usage:

player_three = Player("Donkey Kong", "Standard Kart")

player_three.set_character("Peach")
print(player_three.character)
player_three.set_character("Baby Peach")
print(player_three.character)

"""
Example Output:

Character Updated
Peach
Invalid Character
Peach
"""