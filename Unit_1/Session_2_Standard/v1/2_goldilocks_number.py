""" 
In the extended universe of fictional bears, Goldilocks finds an enticing list of numbers in the Three Bears' house. 
She doesn't want to take a number that's too high or too low - she wants a number that's juuust right. 
Write a function goldilocks_approved() that takes in the list of distinct positive integers nums and returns any number from the list that is neither the minimum 
nor the maximum value in the array, or -1 if there is no such number.
"""

def goldilocks_approved(nums):
    if (len(nums) > 2):
        max_val = max(nums)
        min_val = min(nums)

        for num in nums: 
            if ( num != max_val or num != min_val):
                return num
    return -1 

nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))
