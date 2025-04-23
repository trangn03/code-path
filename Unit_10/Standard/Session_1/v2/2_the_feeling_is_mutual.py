""" 
You are given an insider look into the Hollywood gossip with an adjacency matrix celebrities where each node labeled 0 to n represents a celebrity. celebrities[i][j] = 1 indicates that celebrity i likes celebrity j and celebrities[i][j] = 0 indicates that celebrity i dislikes or doesn't know celebrity j. Write a function is_mutual() that returns True if all relationships between celebrities are mutual and False otherwise. A relationship between two celebrities is mutual if for any celebrity i that likes celebrity j, celebrity j also likes celebrity i.
"""

def is_mutual(celebrities):
    pass

celebrities1 = [
                [0, 1, 1, 0],
                [1, 0, 1, 0],
                [1, 1, 0, 1],
                [0, 0, 1, 0]]

celebrities2 = [
                [0, 1, 1, 0],
                [1, 0, 0, 0],
                [1, 1, 0, 1],
                [0, 0, 0, 0]]

print(is_mutual(celebrities1))
print(is_mutual(celebrities2))

"""
Example Output:

True
False
"""