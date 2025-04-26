""" 
CodePath Airlines uses Breadth First Search to suggest the route with the least number of layovers to its customers. But their software has a bug and is malfunctioning. Help the airline by identifying and fixing the bug.

When properly implemented, the function should accept an adjacency dictionary flights and returns a list with the shortest path from a source location to a destination location.

For this problem:

Identify and fix any bug(s) in the code.
Evaluate the time complexity of the function. Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
If CodePath Airlines used an adjacency matrix instead of an adjacency dictionary/list, would the time complexity change? Why or why not?
"""

from collections import deque

def find_shortest_path(flights, source, destination):
    queue = deque([(source, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == destination:
            return path

        visited.add(current)

        for neighbor in flights.get(current, []):
            if neighbor not in visited:
                queue.append((neighbor, [neighbor]))

    return []

# Example Usage:

flights = {
    'LAX': ['SFO'],
    'SFO': ['LAX', 'ORD', 'ERW'],
    'ERW': ['SFO', 'ORD'],
    'ORD': ['ERW', 'SFO', 'MIA'],
    'MIA': ['ORD']
}

print(find_shortest_path(flights, 'LAX', 'MIA'))

"""
Expected Output:

['LAX', 'SFO', 'JFK', 'MIA']
"""
