"""
You are designing a feature for a podcast app that allows users to reorder their list of episodes. The episodes are initially in a stack (LIFO order). Write a function to reorder the episodes based on a list of indices specifying the new order. The indices are 0-based and represent the new position of each episode in the stack.

For instance, if the stack contains episodes [A, B, C, D] and the indices are [2, 0, 3, 1], it means that the episode originally at index 0 should move to index 2, the episode at index 1 should move to index 0, and so on.

The function should return the reordered list of episodes.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""
def reorder_stack(stack, indices):
  pass
# Example Usage:

stack1 = ['Episode1', 'Episode2', 'Episode3', 'Episode4']
indices = [2, 0, 3, 1]
print(reorder_stack(stack1, indices)) 

stack2 = ['A', 'B', 'C', 'D']
indices = [1, 2, 3, 0]
print(reorder_stack(stack2, indices)) 

stack3 = ['Alpha', 'Beta', 'Gamma']
indices = [0, 2, 1]
print(reorder_stack(stack3, indices)) 
"""
Example Output:

['Episode2', 'Episode4', 'Episode1', 'Episode3']
['D', 'A', 'B', 'C']
['Alpha', 'Gamma', 'Beta']
"""