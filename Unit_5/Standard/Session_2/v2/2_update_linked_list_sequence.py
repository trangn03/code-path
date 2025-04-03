""" 
A linked list is a data structure that allows us to store pieces of data sequentially, similar to a normal list or array. The key difference between a linked list and a normal list is how each element is stored in a computer’s memory.

In a normal list, individual elements are stored in adjacent memory locations according to their order in the list. If we know where the first element is stored, it's easy to access any other element in the list.

In a linked list, individual elements, called nodes, are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes into a sequential list, each node stores a reference or pointer to the next node in the list.

Using the provided Node class and the linked list below, update the current linked list shy_guy -> diddy_kong -> dry_bones to shy_guy -> link -> diddy_kong -> toad -> dry_bones.

A function print_linked_list() that accepts the head, or first element, of a linked list and prints the values of the list has also been provided for testing purposes.
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

shy_guy = Node("Shy Guy")
diddy_kong = Node("Diddy Kong")
dry_bones = Node("Dry Bones")
shy_guy.next = diddy_kong
diddy_kong.next = dry_bones

# Add code to update the list here
# Example Usage:

print("Current List:")
print_linked_list(shy_guy)

"""
Example Output:

Current List:
shy_guy -> diddy_kong -> dry_bones
"""