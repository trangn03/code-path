"""
You're a detective and have been given an anonymous tip on your latest case, but something about it seems fishy - you suspect the clue might be a red herring meant to send you around in circles. Write a function is_circular() that accepts the head of a singly linked list clues and returns True if the tail of the linked list points at the head of the linked list. Otherwise, return False.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(clues):
	pass

# Example Usage:

clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

print(is_circular(clue1))

"""
Example Output:

True
"""