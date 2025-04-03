"""
As a trail worker, you've been tasked with measuring the length of a loop trail that circles back to its starting point. Given the head of a linked list trailhead where each node represents a trail marker and the last marker points back to the first marker, return the length of the trail. Assume the length of the trail is equal to the number of markers.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def trail_length(trailhead):
	pass

# Example Usage:

marker1 = Node("Marker 1")
marker2 = Node("Marker 2")
marker3 = Node("Marker 3")
marker1.next = marker2
marker2.next = marker3
marker3.next = marker1

print(trail_length(marker1))

"""
Example Output:

3
"""