# Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the element at index x in items. If x is not a valid index of items, return None.

def get_item(items, x):
    if  x < len(items) and x >= 0:
        return items[x]
    else:
        return None
    
items = ["piglet", "pooh", "roo", "rabbit"]
x = -1
print(get_item(items, x))
    