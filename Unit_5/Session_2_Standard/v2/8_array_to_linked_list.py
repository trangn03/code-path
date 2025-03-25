""" 
Write a function arr_to_ll() that accepts an array of Player instances arr and converts arr into a linked list. The function should return the head of the linked list. If arr is empty, return None.

A function print_linked_list() which accepts the head, or first element, of a linked list and prints the character attribute of each Player in the linked list has also been provided for testing purposes.
"""

class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value.character, end=" -> " if current.next else "\n")
        current = current.next

def arr_to_ll(arr):
    pass

# Example Usage:

mario = Player("Mario", "Mushmellow")
luigi = Player("Luigi", "Standard LG")
peach = Player("Peach", "Bumble V")

print_linked_list(arr_to_ll([mario, luigi, peach]))
print_linked_list(arr_to_ll([peach]))

"""
Example Output:

Mario -> Luigi -> Peach
Peach
"""