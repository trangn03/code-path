""" 
You're tasked with identifying trending memes. A meme is considered "trending" if it appears in the dataset multiple times.

Write the find_trending_memes() function, which takes a list of meme texts and returns a list of trending memes, where a trending meme is defined as a meme that appears more than once in the list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

def find_trending_memes(memes):
    pass

# Example Usage:

memes = ["Dogecoin to the moon!", "One does not simply walk into Mordor", "Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine", "Surprised Pikachu", "Surprised Pikachu"]
memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

print(find_trending_memes(memes))
print(find_trending_memes(memes_2))
print(find_trending_memes(memes_3))

"""
Example Output:

['Dogecoin to the moon!', 'One does not simply walk into Mordor']
['Surprised Pikachu']
[]
"""