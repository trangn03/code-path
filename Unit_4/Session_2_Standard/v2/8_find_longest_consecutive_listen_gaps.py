"""
You are building a feature for a podcast app that helps users identify the longest period of time between listening to consecutive episodes of a podcast. Given a list of episode listen timestamps (in minutes since midnight) sorted in ascending order, your task is to determine the longest gap between consecutive listens.

Write a function to find the longest gap between consecutive listens.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""
def find_longest_gap(timestamps):
  pass
# Example Usage:

timestamps1 = [30, 50, 70, 100, 120, 150]
print(find_longest_gap(timestamps1))

timestamps2 = [10, 20, 30, 50, 60, 90]
print(find_longest_gap(timestamps2))

timestamps3 = [5, 10, 15, 25, 35, 45]
print(find_longest_gap(timestamps3))

"""
Example Output:

30
30
10
"""