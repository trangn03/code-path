"""
Players can pick up special items as they race.

Update the Player class with a new method add_item() that takes in one parameter, item_name.

The method should validate the item_name.

If the item is valid, add item_name to the player’s items attribute.
The method does not need to return any values.
item_name is valid if it has one of the following values: "banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill". 
"""
class Player():
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
        
    def add_item(self, item_name):
        pass
    
# Example Usage:

player_one = Player("Yoshi", "Dolphin Dasher")

print(player_one.items)

player_one.add_item("red shell")
print(player_one.items)

player_one.add_item("super star")
print(player_one.items)

player_one.add_item("super smash")
print(player_one.items)
"""
Example Output:

[]
['red shell']
['red shell', 'super star']
['red shell', 'super star', 'super smash']
"""