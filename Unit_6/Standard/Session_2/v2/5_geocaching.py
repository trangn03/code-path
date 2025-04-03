"""
You are hiking on a trail that has a geocache hidden at each marker. Each cache is also labeled with a 0 or 1. The geocaches are arranged in a sequence, forming a binary code that represents the coordinates of a special, hidden cache. The most significant bit is at the first marker on the trail. Given the head of a linked list cache_labels representing the sequence of 0s and 1s you found at each marker, write a function locate_cache() that decodes the sequence and returns the decimal value of the hidden cache's coordinates.
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

def locate_cache(cache_labels):
    pass

# Example Usage:

cache_labels = Node(1, Node(0, Node(1))) # 101 base 2

print(locate_cache(cache_labels))

"""
Example Output:

5
Explanation: (101) in base 2 = (5) in base 10
"""