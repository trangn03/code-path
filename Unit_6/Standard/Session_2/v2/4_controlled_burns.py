"""
You are working with local foresters on a section of trail through local wilderness with particularly dense forests. 
The foresters recommend doing controlled burns on certain sections of the forest to help decrease severe wildfire risk and promote biodiversity 
which means certain parts of the trail will be off limits for the upcoming season. Given the head of a linked list of trail markers, trailhead and two integers m and n, 
write a function to traverse the trail, keeping only the first m markers, and then removing the next n markers. 
Continue this pattern until the end of the trail is reached. Return the head of the updated trail.
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

def selective_trail_clearing(trailhead, m, n):
    pass

# Example usage:

trailhead = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10))))))))))

print_linked_list(selective_trail_clearing(trailhead, 2, 3))

"""
Example Output:

1 -> 2 -> 6 -> 7 -> 11 -> 12
Explanation: Keep the first (m = 2) nodes starting from the head of the linked List  
(1 -> 2) show in black nodes.
Delete the next (n = 3) nodes (3 -> 4 -> 5) show in red nodes.
Continue with the same procedure until reaching the tail of the Linked List.
"""