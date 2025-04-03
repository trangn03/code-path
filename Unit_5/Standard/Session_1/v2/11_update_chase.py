"""
Using the linked list from Problem 10, remove the dog node and add in a node cheese with value "Gouda" to the end of the list so that the resulting list is cat -> mouse -> cheese.
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next