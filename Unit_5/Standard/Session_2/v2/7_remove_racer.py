""" 
Write a function remove_racer() that takes in the head of a linked list and a value racer as parameters.

The function should remove the first node with the value racer from the linked list and return the head of the modified list. If racer is not in the list, return the head of the original list.
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

def remove_racer(head, racer):
    pass

# Example Usage:

head = Node("Daisy", Node("Mario", Node("Toad", Node("Mario"))))

# Linked List: Daisy -> Mario -> Toad -> Mario
print_linked_list(remove_racer(head, "Mario"))

# Linked List: Daisy -> Mario -> Toad
print_linked_list(remove_racer(head, "Yoshi"))

"""
Example Output:

Daisy -> Mario -> Toad
Daisy -> Mario -> Toad
"""