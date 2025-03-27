""" 
You are managing a podcast and need to analyze the lengths of the episodes. Given a list of episodes where each episode is represented by its duration in minutes, you want to determine how many episodes fall into each of the following time ranges: less than 30 minutes, 30 to 60 minutes, and more than 60 minutes.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

def track_episode_lengths(episode_lengths):
  pass

# Example Usage:

episode_lengths = [15, 45, 32, 67, 22, 59, 70]
print(track_episode_lengths(episode_lengths))

episode_lengths_2 = [10, 25, 30, 45, 55, 65, 80]
print(track_episode_lengths(episode_lengths_2))

episode_lengths_3 = [30, 30, 30, 30, 30]
print(track_episode_lengths(episode_lengths_3))

"""
Example Output:

(2, 3, 2)
(2, 3, 2)
(0, 5, 0)
"""