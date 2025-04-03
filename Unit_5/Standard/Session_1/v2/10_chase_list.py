"""
In a linked list, pointers can be redirected at any place in the list.

Using the linked list from Problem 9, create a new Node dog with value "Spike" and point it to the cat node so that the full list now looks like dog -> cat -> mouse. 
"""

# Example Usage:

print(dog.value)
print(dog.next)
print(dog.next.value)
print(cat.next)
print(cat.next.value)
print(mouse.next.value)

"""
Example Output:

Spike
cat
Tom
mouse
Jerry
None
"""
