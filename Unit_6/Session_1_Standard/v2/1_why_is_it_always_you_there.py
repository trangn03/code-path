""" 
In a single assignment statement, create the linked list Harry -> Ron -> Hermione.
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

# Add your assignment statement here

# Example Usage:

print_linked_list(head)

"""
Expected Output:

Harry -> Ron -> Hermione
"""