""" 
A spell gone wrong has reversed time! Write a function reverse() that accepts the head of a singly linked list events and restores order by reversing the order of elements. Return the head of the reversed list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
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

def reverse(events):
    pass

# Example Usage:

events = Node("Potion Brewing", 
            Node("Spell Casting", 
                Node("Wand Making", 
                    Node("Dragon Taming", 
                        Node("Broomstick Flying")))))

print_linked_list(reverse(events))

"""
Example Output:

Broomstick Flying -> Dragon Taming -> Wand Making -> Spell Casting -> Potion Brewing
"""