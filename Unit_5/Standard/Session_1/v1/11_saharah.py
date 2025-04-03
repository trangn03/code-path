""" 
Using the linked list from Problem 10, 
remove the tom_nook node and add in a node saharah with value "Saharah" to the end of the list so that the resulting list is timmy -> tommy -> saharah.
"""

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

tom_nook = Node("Tom Nook")
timmy = Node("Timmy")
tommy = Node("Tommy") 
saharah = Node("Saharah")

timmy.next = tommy
tommy.next = saharah

print(tom_nook.next) 
print(timmy.value) 
print(timmy.next.value)  
print(tommy.value) 
print(tommy.next.value)
print(saharah.value)  
print(saharah.next) 