""" 
You need to analyze the trends of various memes over time. You have a dataset where each meme has a name, a list of daily popularity scores (number of reposts each day), and other metadata.

Write the find_trending_meme() function, which takes in a list of memes (each with a name and a list of daily repost counts) and a time range (represented by a start and end day, inclusive). The function should return the name of the meme with the highest average reposts over the specified period. If there is a tie, return the meme that appears first in the list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

def find_trending_meme(memes, start_day, end_day):
    pass

# Example Usage:

memes = [
    {"name": "Distracted boyfriend", "reposts": [5, 3, 2, 7, 6]},
    {"name": "Dogecoin to the moon!", "reposts": [2, 4, 6, 8, 10]},
    {"name": "One does not simply walk into Mordor", "reposts": [3, 3, 5, 4, 2]}
]

memes_2 = [
    {"name": "Surprised Pikachu", "reposts": [2, 1, 4, 5, 3]},
    {"name": "This is fine", "reposts": [3, 5, 2, 6, 4]},
    {"name": "Expanding brain", "reposts": [4, 2, 1, 4, 2]}
]

memes_3 = [
    {"name": "Y U No?", "reposts": [1, 2, 1, 2, 1]},
    {"name": "Philosoraptor", "reposts": [3, 1, 3, 1, 3]}
]
print(find_trending_meme(memes, 1, 3))
print(find_trending_meme(memes_2, 0, 2))
print(find_trending_meme(memes_3, 2, 4))

"""
Example Output:

Dogecoin to the moon!
This is fine
Philosoraptor
"""