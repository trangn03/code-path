""" 
You want to track the most popular destinations you visited based on the number of times you have visited them. Given a list of visited destinations with timestamps, your goal is to determine the destination that has been visited the most and the total number of times it was visited. If there is a tie, return the one with the latest visit.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

def most_popular_destination(visits):
  pass

# Example Usage:

visits = [("Paris", "2024-07-15"), ("Tokyo", "2024-08-01"), ("Paris", "2024-08-05"), ("New York", "2024-08-10"), ("Tokyo", "2024-08-15"), ("Paris", "2024-08-20")]
print(most_popular_destination(visits))

visits_2 = [("London", "2024-06-01"), ("Berlin", "2024-06-15"), ("London", "2024-07-01"), ("Berlin", "2024-07-10"), ("London", "2024-07-15")]
print(most_popular_destination(visits_2))

visits_3 = [("Sydney", "2024-05-01"), ("Dubai", "2024-05-15"), ("Sydney", "2024-05-20"), ("Dubai", "2024-06-01"), ("Dubai", "2024-06-15")]
print(most_popular_destination(visits_3))

"""
Example Output:

('Paris', 3)
('London', 3)
('Dubai', 3)
"""