""" 
In a nearby enchanted forest, magical paths sometimes loop back on themselves, creating never-ending cycles. Write a function loop_start() to help you keep your way. The function accepts the head of a linked list path_start and returns the value of the node where the cycle starts. If the path has no cycle, return None.

A linked list has a cycle if, at some point in the list, the node’s next pointer points back to a previous node in the list.

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

def loop_start(path_start):
    pass

# Example Usage:

path_start = Node("Mystic Falls")
waypoint1 = Node("Troll's Bridge")
waypoint2 = Node("Elven Arbor")
waypoint3 = Node("Fairy Glade")

path_start.next = waypoint1
waypoint1.next = waypoint2
waypoint2.next = waypoint3
waypoint3.next = waypoint1

print(loop_start(path_start))

"""
Example Output:

Troll's Bridge
"""