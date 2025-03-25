""" 
Write a function copy_ll() that takes in the head of a linked list and creates a complete copy of that linked list.

The function should return the head of a new linked list which is identical to the given list in terms of its structure and contents, but does not use any of the node objects from the original list.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def copy_ll(head):
    pass

# Example Usage:

mario = Node("Mario")
daisy = Node("Daisy")
luigi = Node("Luigi")
mario.next = daisy
daisy.next = luigi

# Linked List: Mario -> Daisy -> Luigi
copy = copy_ll(mario)

# Change original list -- should not affect the copy
mario.value = "Original Mario"

print_linked_list(head)
print_linked_list(copy) 

"""
Example Output:

Original Mario -> Daisy -> Luigi
Mario -> Daisy -> Luigi
"""
