""" 
The following graph illustrates connections between different Hollywood stars. Each node represents a celebrity, and an edge between two nodes indicates that the celebrities know each other.

Create a variable hollywood_stars that represents the undirected graph below as an adjacency dictionary, where each node's value is represented by a string with the airport's name (ex. "Kevin Bacon").
"""

# Example Usage:

print(list(hollywood_stars.keys()))
print(list(hollywood_stars.values()))
print(hollywood_stars["Kevin Bacon"])

"""
Example Output:

['Kevin Bacon', 'Meryl Streep', 'Idris Elba', 'Laverne Cox', 'Sofia Vergara']
[['Laverne Cox', 'Sofia Vergara'], ['Idris Elba', 'Sofia Vergara'], ['Meryl Streep', 'Laverne Cox'], 
['Kevin Bacon', 'Idris Elba'], ['Kevin Bacon', 'Meryl Streep']]
['Laverne Cox', 'Sofia Vergara']
"""