"""
In your work with a wildlife conservation database, you have two lists: observed_species and priority_species. 
The elements of priority_species are distinct, and all elements in priority_species are also in observed_species.
Write a function prioritize_observations() that sorts the elements of observed_species such that the relative ordering of items in observed_species matches that of priority_species. 
Species that do not appear in priority_species should be placed at the end of observed_species in ascending order. 
"""

def prioritize_observations(observed_species, priority_species):
  pass

# Example Usage:

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 

# Expected Output:

# ["🐯", "🐯", "🐯", "🦌", "🐘", "🦁", "🦁", "🐻", "🦑", "🐼", "🐍"]
# ["cardinal", "sparrow", "bluejay", "crow", "robin"]