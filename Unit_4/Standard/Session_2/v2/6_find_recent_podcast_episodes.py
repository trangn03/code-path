"""
You are developing a podcast management system and need to keep track of the most recent podcast episodes. Given a list of episodes where each episode is represented by a unique ID, you need to implement a function that retrieves the most recent n episodes from the list in the order they were added.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""
def get_recent_episodes(episodes, n):
  pass
# Example Usage:

episodes1 = ['episode1', 'episode2', 'episode3', 'episode4']
n = 3
print(get_recent_episodes(episodes1, n))

episodes2 = ['ep1', 'ep2', 'ep3']
n = 2
print(get_recent_episodes(episodes2, n))

episodes3 = ['a', 'b', 'c', 'd']
n = 5
print(get_recent_episodes(episodes3, n))

"""
Example Output:

['episode4', 'episode3', 'episode2']
['ep3', 'ep2']
['d', 'c', 'b', 'a']
"""