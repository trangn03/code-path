""" 
As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical, meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. 
Given a post title as a string, use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.
"""
# Same as valid palindrome
def is_symmetrical_title(title):
    # Left as start of title
    left = 0
    # Right as the end of title 
    right = len(title) - 1
    while left < right: 
        # Move `left` pointer to the right if the current character is not alphanumeric.
        while left < right and not title[left].isalnum():
            left += 1
        # Move `right` pointer to the left if the current character is not alphanumeric.
        while left < right and not title[right].isalnum():
            right -= 1
        # Compare the characters at `left` and `right`
        # If they don't match, return False
        # If they do match, move both pointers towards the center 
        if left < right:
            if title[left].lower() != title[right].lower():
                return False
            left += 1
            right -= 1
    # If all characters match, return True 
    return True 

# Example Usage:

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 

"""
Example Output:

True
False
"""