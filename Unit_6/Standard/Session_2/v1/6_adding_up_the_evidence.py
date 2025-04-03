"""
You have all your evidence, and it's time to sum it to the final answer! You are given the heads of two non-empty non-empty linked lists head_a and head_b representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

The digits of the sum should also be stored in reverse order with each node containing a single digit.

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

def add_two_numbers(head_a, head_b):
    pass

# Example Usage:
head_a = Node(2, Node(4, Node(3))) # 342
head_b = Node(5, Node(6, Node(4))) # 465

print_linked_list(add_two_numbers(head_a, head_b))

"""
Example Output:

7 -> 0 -> 8
Explanation: 342 + 465 = 807 
"""
