"""
The Villager class has been updated below to include the new string attribute personality representing the character's personality type.
Outside of the Villager class, write a function of_personality_type(). 
Given a list of Villager instances townies and a string personality_type as parameters, return a list containing the names of all villagers in townies with personality personality_type. 
Return the names in any order.
"""

class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
    # ... methods from previous problems
    
def of_personality_type(townies, personality_type):
    lst = []
    for i in townies:
        if i.personality == personality_type:
            lst.append(i.name)
    return lst

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))


"""
Example Output:

["Bob", "Stitches"]
[]
"""