""" 
There are n users in a queue waiting to stream their favorite movies, where the 0th user is at the front of the queue and the (n - 1)th user is at the back of the queue.

You are given a 0-indexed integer array movies of length n where the number of movies that the ith user would like to stream is movies[i].

Each user takes exactly 1 second to stream a movie. A user can only stream 1 movie at a time and has to go back to the end of the queue (which happens instantaneously) in order to stream more movies. If a user does not have any movies left to stream, they will leave the queue.

Return the time taken for the user at position k (0-indexed) to finish streaming all their movies.
"""

def time_required_to_stream(movies, k):
  pass

# Example Usage:

print(time_required_to_stream([2, 3, 2], 2)) 
print(time_required_to_stream([5, 1, 1, 1], 0)) 

# Example Output:

# 6
# 8