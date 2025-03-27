""" 
You're tasked with analyzing the order in which memes gain popularity. Memes are posted in a sequence, and their popularity grows as they are reposted.

Write the simulate_meme_reposts() function, which takes a list of memes (representing their initial posting order) and simulate their reposting by processing each meme in the queue. Each meme can be reposted multiple times, and for each repost, it should be added back to the queue. The function should return the final order in which all reposts are processed.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""
def simulate_meme_reposts(memes, reposts):
    pass

# Example Usage:

memes = ["Distracted boyfriend", "Dogecoin to the moon!", "One does not simply walk into Mordor"]
reposts = [2, 1, 3]

memes_2 = ["Surprised Pikachu", "This is fine", "Expanding brain"]
reposts = [1, 2, 2]

memes_3 = ["Y U No?", "Philosoraptor"]
reposts = [3, 1]

print(simulate_meme_reposts(memes, reposts))
print(simulate_meme_reposts(memes_2, reposts))
print(simulate_meme_reposts(memes_3, reposts))

"""
Example Output:

['Distracted boyfriend', 'Dogecoin to the moon!', 'One does not simply walk into Mordor', 'Distracted boyfriend', 'One does not simply walk into Mordor', 'One does not simply walk into Mordor']
['Surprised Pikachu', 'This is fine', 'Expanding brain', 'This is fine', 'Expanding brain']
['Y U No?', 'Philosoraptor', 'Y U No?', 'Y U No?']
"""