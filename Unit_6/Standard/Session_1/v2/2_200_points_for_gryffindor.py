""" 
It's almost the end of the year, and Gryffindor students want to see if they have any competition for first place. Given the head of a linked list house_points and the Gryffindor's score, return the frequency of score in the list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

class Node:
    def __init__(self, house, score, next=None):
        self.house = house
        self.value = score 
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print((current.house, current.value), end=" -> " if current.next else "\n")
        current = current.next

def count_element(house_points, score):
	pass
# Example Usage:

house_points = Node("Gryffindor", 600, 
                Node("Ravenclaw", 300,
                    Node("Slytherin", 500,
                        Node("Hufflepuff", 600))))

print(count_element(house_points, score))

"""
Example Output:

2
"""