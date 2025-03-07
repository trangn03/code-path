"""
NASA has asked the public to vote on a new name for one of the nodes in the International Space Station. 
Given a list of strings votes where each string in the list is a voter's suggested new name, 
implement a function get_winner() that returns the suggestion with the most number of votes.
If there is a tie, return either option. 
"""

def get_winner(votes):
    pass

# Example Usage:

votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]

print(get_winner(votes1))
print(get_winner(votes2))

"""
Example Output:

Colbert
Serenity

Note: Colbert and Serenity would both be acceptable answers for the second example
"""