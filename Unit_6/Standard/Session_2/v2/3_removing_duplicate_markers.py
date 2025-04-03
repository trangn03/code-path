"""
When clearing an old trail, you notice some markers have been placed more than once, confusing hikers. 
Given the head of a sorted linked list of numbered trail markers, trailhead, write a function that removes all duplicate markers, keeping only the unique ones. 
Return the head of the updated trail.
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

def remove_duplicate_markers(trailhead):
    pass

# Example Usage:

trailhead = Node(1, Node(2, Node(3, Node(3, Node(4)))))

print_linked_list(remove_duplicate_markers(trailhead))

"""
Example Output:

1 -> 2 -> 4
Explanation: 3 appears more than once so it is deleted from the list
"""