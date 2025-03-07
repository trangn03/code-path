"""
Ground control has sent a transmission containing important information. 
A complete transmission is one where every letter of the English alphabet appears at least once.
Given a string transmission containing only lowercase English letters, return true if the transmission is complete, or false otherwise. 
"""

def check_if_complete_transmission(transmission):
    """
    :type transmission: str
    :rtype: bool
    """
    
# Example Usage:

transmission1 = "thequickbrownfoxjumpsoverthelazydog"
transmission2 = "spacetravel"

print(check_if_complete_transmission(transmission1))
print(check_if_complete_transmission(transmission2))

# Example Output:

# True
# False