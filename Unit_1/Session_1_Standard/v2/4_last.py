"""
Implement a function get_last() that accepts a list of items items 
and returns the last item in the list. 
If the list is empty, return None. 
"""

def get_last(items):
    if items:  
        return items[-1]  
    else:
        return None 


items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
print(get_last(items))

items = []
get_last(items)