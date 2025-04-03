""" 
You are given a 2D integer array trips and two integers start_dest and end_dest. Each trips[i] = [starti, endi] represents an inclusive travel interval between starti and endi.

Return True if each destination in the inclusive route [start_dest, end_dest] is covered by at least one trip in trips. Return False otherwise.

A destination x is covered by a trip trips[i] = [starti, endi] if starti <= x <= endi.
"""

def is_route_covered(trips, start_dest, end_dest):
  pass

# Example Usage:

trips1 = [[1, 2], [3, 4], [5, 6]]
start_dest1, end_dest1 = 2, 5

trips2 = [[1, 10], [10, 20]]
start_dest2, end_dest2 = 21, 21

trips3 = [[1, 2], [3, 5]]
start_dest3, end_dest3 = 2, 5

print(is_route_covered(trips1, start_dest1, end_dest1))
print(is_route_covered(trips2, start_dest2, end_dest2))
print(is_route_covered(trips3, start_dest3, end_dest3))

# Example Output:

# True
# False
# True
