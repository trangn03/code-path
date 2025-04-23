""" 
You are a pilot navigating a new airport and have a map of the airport represented as an undirected star graph with n nodes where each node represents a terminal in the airport labeled from 1 to n. You want to find the center terminal in the airport where the pilots' lounge is located.

Given a 2D integer array terminals where each terminal[i] = [u, v] indicates that there is a path (edge) between terminal u and v, return the center of the given airport.

A star graph is a graph where there is one center node and exactly n-1 edges connecting the center node ot every other node.
"""

def find_center(terminals):
    pass

terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

print(find_center(terminals1))
print(find_center(terminals2))
"""
Example Output:

2
1
"""