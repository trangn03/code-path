"""
Write a function squared() that accepts a list of integers numbers as a parameter and squares each item in the list. 
Return the squared list. 
"""

def squared(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i]**2
    return numbers

# Example Usage: 
numbers = [1, 2, 3]
print(squared(numbers))