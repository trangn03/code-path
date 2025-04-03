"""
A new witness has emerged and provided a new account of events the night of the crime. Given the heads of two sorted linked lists, known_timeline and witness_timeline, each representing a numbered sequence of events, merge the two timelines into one sorted sequence of events. The resulting linked list should be made by splicing together the nodes of the first two timelines. Return the head of the merged timeline.

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

def merge_timelines(known_timeline, witness_timeline):
	pass

# Example Usage:

known_timeline = Node(1, Node(2, Node(4)))
witness_timeline = Node(1, Node(3, Node(4)))

print_linked_list(merge_timelines(known_timeline, witness_timeline))

"""
Example Output:

1 -> 1 -> 2 -> 3 -> 4 -> 4
"""