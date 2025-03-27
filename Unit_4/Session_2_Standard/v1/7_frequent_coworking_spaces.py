""" 
You often work from various co-working spaces. 
You want to analyze your usage patterns to identify which co-working spaces you visit the most frequently. Given a list of co-working spaces you visited over the past month, write a function to determine which co-working space(s) you visited most frequently. If there is a tie, return all of the most visited spaces.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""
def most_frequent_spaces(visits):
  pass

# Example Usage:

visits = ["WeWork", "Regus", "Spaces", "WeWork", "Regus", "WeWork"]
print(most_frequent_spaces(visits))

visits_2 = ["IndieDesk", "Spaces", "IndieDesk", "WeWork", "Spaces", "IndieDesk", "WeWork"]
print(most_frequent_spaces(visits_2))

visits_3 = ["Hub", "Regus", "WeWork", "Hub", "WeWork", "Regus", "Hub", "Regus"]
print(most_frequent_spaces(visits_3))

"""
Example Output:

['WeWork']
['IndieDesk']
['Hub', 'Regus']
"""
