"""
You are given an array paths, where paths[i] = [hubA, hubB] means there exists a direct communication path going from hubA to hubB. 
Return the final communication hub, that is, the hub without any outgoing path to another hub.
It is guaranteed that the paths form a line without any loops, therefore, there will be exactly one final communication hub. 
"""

def find_final_hub(paths):
    pass
# Example Usage:

paths1 = [["Earth", "Mars"], ["Mars", "Titan"], ["Titan", "Europa"]]
paths2 = [["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]]
paths3 = [["StationA", "StationZ"]]

print(find_final_hub(paths1)) 
print(find_final_hub(paths2)) 
print(find_final_hub(paths3))

# Example Output:

# "Europa"
# "Delta"
# "StationZ"