""" 
Update the Villager class with a method print_inventory() that accepts no parameters except for self.

The method should print the name and quantity of each item in a villager’s furniture list.

The name and quantity should be in the format "item1: quantity, item2: quantity, item3: quantity" for however many unique items exist in the villager's furniture list
If the player has no items, the function should print "Inventory empty".
"""
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
        
    def print_inventory(self):
        # Empty dictionary
        if not self.furniture:
            print("Inventory empty")
        else:
            item_count = {}
            for i in self.furniture:
                if i in item_count:
                    item_count[i] += 1
                else:
                    item_count[i] = 1
            print(", ".join([f"{i}: {count}" for i, count in item_count.items()]))
        
        
alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()