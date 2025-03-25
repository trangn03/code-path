"""
One of the drawbacks of a linked list is that it's difficult to go backwards, because each Node only knows about the Node in front of it. (E.g., A -> B -> C)

A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked list also has a prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

Update the code below to convert the singly linked list to a doubly linked list.

Two functions, print_linked_list() and print_linked_list_backwards(), have been provided for testing purposes. print_linked_list() accepts the head of a linked list and prints the values of each node in the list, starting at the head and iterating in a forward direction. print_linked_list_backwards() accepts the tail of a linked list and prints the values of each node in the list, starting at the tail and iterating in a backward direction.
"""
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

koopa_troopa = Node("Koopa Troopa")
toadette = Node("Toadette")
waluigi = Node("Waluigi")
koopa_troopa.next = toadette
toadette.next = waluigi

# Add code to convert to doubly linked list here
# Example Usage:

print_linked_list(koopa_troopa)
print_linked_list_backwards(waluigi)

"""
Example Output:

Koopa Troopa -> Toadette -> Waluigi
Waluigi -> Toadette -> Koopa Troopa
"""