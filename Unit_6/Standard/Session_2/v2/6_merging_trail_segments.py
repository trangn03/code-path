"""
While constructing a new trail, you’ve set up several segments separated by temporary markers. Once the segments are ready, you want to merge them into continuous trails. Given the head of a linked list of trail markers trailhead, merge the nodes between the temporary markers (0s) by summing their values into a single marker. The final trail should not contain any temporary markers. Return the head of the merged trail.

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

def merge_trail(trailhead):
    pass

# Example Usage:


trail1 = Node(0, Node(3, Node(1, Node(0, Node(4, Node(5, Node(4, Node(2, Node(0)))))))))
trail2 = Node(0, Node(1, Node(0, Node(3, Node(0, Node(2, Node(2, Node(0))))))))

print_linked_list(merge_trail(trail1))
print_linked_list(merge_trail(trail2))

"""
Example Output:

4 -> 11
Example 1 Explanation: 
The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.

1 -> 3 -> 4
Example 2 Explanation: The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4.
"""