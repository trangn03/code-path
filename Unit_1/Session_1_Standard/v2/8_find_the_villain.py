"""
Write a function find_villain() that accepts a list crowd and a value villain as parameters 
and returns a list of all indices where the villain is found hiding in the crowd. 
"""


def find_villain(crowd, villain):
    # Initialize a new list 
    list_indices = []
    index = 0
    
    # Go through all of the list of crowd 
    # If the villain contains the crowd 
    for i in crowd:
        if i == villain:
            list_indices.append(index)
        index += 1
    return list_indices
            
    # Slicing: start, stop, step
    # return list_indices

# Example Usage

crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
villain = 'The Joker'
print(find_villain(crowd, villain))

# Example Output:

[1, 4, 6]