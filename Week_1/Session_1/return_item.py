def get_item(items, x):
    if  x < len(items) and x >= 0:
        return items[x]
    else:
        return None
    
items = ["piglet", "pooh", "roo", "rabbit"]
x = -1
print(get_item(items, x))
    