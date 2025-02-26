"""
Write a function up_and_down() that accepts a list of integers lst as a parameter. 
The function should return the number of odd numbers minus the number of even numbers in the list. 
"""

def up_and_down(lst):
    # Initialize odd and even counter for the list 
    even_count = 0
    odd_count = 0
    
    # Loop all of integers in the list
    for i in lst: 
        # Check if the integers is odd or even
        # Count the number in the list 
        if i % 2 != 0:
            odd_count += 1
        else:
            even_count += 1
    return odd_count - even_count
    # Return the number of odd numbers minus the number of even numbers 


# Example Usage

lst = [1, 2, 3] # 2 odd 1 even -> 2-1
print(up_and_down(lst))

lst = [1, 3, 5] # 3 odd 0 even -> 3-0
print(up_and_down(lst))

lst = [2, 4, 10, 2] # 0 odd 4 even -> 0-4 
print(up_and_down(lst))

# Example Output:

"""
1
3
-4
"""