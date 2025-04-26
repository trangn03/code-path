""" 
If you solved the above problem can_rebook() using Breadth First Search, try solving it using Depth First Search. If you solved it using Depth First Search, solve it using Breadth First Search.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
"""

def can_rebook(flights, source, dest):
    pass
# Example Usage:

flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]

flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2)) 
"""
Example Output:

True
False
"""