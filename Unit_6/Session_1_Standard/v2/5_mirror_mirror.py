""" 
You think another bit of wonky spell casting may have left your enchanted mirror broken. Write a function is_mirrored() to test if your mirror successfully reflects objects back. The function accepts the head of a linked list and should return True if the values of the linked list read the same backwards and forwards, and False otherwise.

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

def is_mirrored(head):
	pass

# Example Usage:

list1 = Node("Phoenix", Node("Dragon", Node("Phoenix")))
list2 = Node("Werewolf", Node("Vampire", Node("Griffin")))

print(is_mirrored(list1))
print(is_mirrored(list2))

"""
Example Output:

True
False
"""