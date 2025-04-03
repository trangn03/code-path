"""
You're having a tough time making a break in the case, and it's time to shake things up to gain a new perspective. Given the head of a linked list of numbered pieces of evidence evidence, and a non-negative integer k, rotate the list to the right by k places. Return the head of the rotated list.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
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

def rotate_right(head, k):
	pass

# Example Usage: 
evidence_list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
evidence_list2 = Node(0, Node(1, Node(2)))

print_linked_list(rotate_right(evidence_list1, 2))
print_linked_list(rotate_right(evidence_list2, 4))

"""
Example Output:

4 -> 5 -> 1 -> 2 -> 3
2 -> 0 -> 1
"""