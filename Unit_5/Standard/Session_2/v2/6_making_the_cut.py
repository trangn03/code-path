""" 
Imagine that a linked list is used to track the order players finished in a race. Write a function top_n_finishers() that takes in the head of a linked list and a non-negative integer n as parameters.

The function should return a list of the values of the first n nodes.

If n is greater than the length of the linked list, return a list of the values of all nodes in the linked list.
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

def top_n_finishers(head, n):
    pass

# Example Usage:

head = Node("Daisy", Node("Mario", Node("Toad", Node("Yoshi"))))

# Linked List: Daisy -> Mario -> Toad -> Yoshi
print(top_n_finishers(head, 3))

# Linked List: Daisy -> Mario -> Toad -> Yoshi
print(top_n_finishers(head, 5))

"""
Example Output:

["Daisy", "Mario", "Toad"]
["Daisy", "Mario", "Toad", "Yoshi"]
"""