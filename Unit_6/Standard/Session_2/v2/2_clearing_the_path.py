"""
While maintaining a trail, you discover that some parts of the path loop back on themselves, creating confusing detours. Given the head of a linked list that may contain cycles trailhead, wite a function that removes any loops/cycles in the trail ensuring a clear, straightforward path. Return the head of the cleared trail.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing - careful this will cause an infinite loop when used on a list w/cycles
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def clear_trail(trailhead):
	pass

# Example Usage:

marker1 = Node("Trailhead")
marker2 = Node("Trail Fork")
marker3 = Node("The Falls")
marker4 = Node("Peak")
marker1.next = marker2
marker2.next = marker3
marker3.next = marker4
marker4.next = marker2

print_linked_list(clear_trail(marker1))

"""
Example Output:

Trailhead -> Trail Fork -> The Falls -> Peak
"""