""" 
Write a function get_length() that takes in a node at an unknown position within a doubly linked list. The function should return the length of the entire list.
"""

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def get_length(node):
    pass  

# Example Usage:

yoshi_falls = Node("Yoshi Falls")
moo_moo_farm = Node("Moo Moo Farm")
rainbow_road = Node("Rainbow Road")
dk_mountain = Node("DK Mountain")
yoshi_falls.next = moo_moo_farm
moo_moo_farm.next = rainbow_road
rainbow_road.next = dk_mountain
dk_mountain.prev = rainbow_road
rainbow_road.prev = moo_moo_farm
moo_moo_farm.prev = yoshi_falls

# List: Yoshi Falls <-> Moo Moo Farm <-> Rainbow Road <-> DK Mountain
print(get_length(rainbow_road))
"""
Example Output:

4
"""