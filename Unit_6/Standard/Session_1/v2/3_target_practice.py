""" 
You are practicing the accuracy of your spellwork by trying to extract the middle-most ingredient in a line of potions. Given the head of a linked list, potions, use a variation of the two-pointer technique to return the middle potion. If there are two middle nodes, return the potion of the second middle node.

The two-pointer variation you should use is called the 'slow and fast pointer' or 'tortoise and the hare' technique. In this variation, a slow and a fast pointer are incremented at different rates.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

class Node:
    def __init__(self, potion, next=None):
        self.potion = potion
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.potion, end=" -> " if current.next else "\n")
        current = current.next

def find_middle_potion(potions):
	pass

# Example Usage:

potions1 = Node("Poison Antidote", Node("Shrinking Solution", Node("Trollblood Tincture")))
potions2 = Node("Elixir of Life", Node("Sleeping Draught", Node("Babbling Beverage", Node("Aging Potion"))))

print(find_middle_potion(potions1))
print(find_middle_potion(potions2))

"""
Example Output:

Shrinking Solution
Sleeping Draught
"""