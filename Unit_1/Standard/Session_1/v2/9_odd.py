"""
Write a function get_odds() that takes in a list of integers nums 
and returns a new list containing all the odd numbers in nums. 
"""

def get_odds(nums):
    # Initialize new list
	new_list = []
	# Loops all the num in the list
	for i in nums: 
	# Using modulo to check if mod % 2 != 0 
	# If yes then append the number into the list 
		if i % 2 != 0:
			new_list.append(i)
	# Return new list
	return new_list


#Example Usage

nums = [1, 2, 3, 4]
print(get_odds(nums))

nums = [2, 4, 6, 8]
print(get_odds(nums))

# Example Output:

"""
[1, 3]
[]
"""