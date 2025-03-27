""" 
You want to identify the top meme creators based on the number of memes they have created.

Write the count_meme_creators() function, which takes a list of meme dictionaries and returns the creators' names and the number of memes they have created.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

def count_meme_creators(memes):
    pass

# Example Usage:

memes = [
    {"creator": "Alex", "text": "Meme 1"},
    {"creator": "Jordan", "text": "Meme 2"},
    {"creator": "Alex", "text": "Meme 3"},
    {"creator": "Chris", "text": "Meme 4"},
    {"creator": "Jordan", "text": "Meme 5"}
]

memes_2 = [
    {"creator": "Sam", "text": "Meme 1"},
    {"creator": "Sam", "text": "Meme 2"},
    {"creator": "Sam", "text": "Meme 3"},
    {"creator": "Taylor", "text": "Meme 4"}
]

memes_3 = [
    {"creator": "Blake", "text": "Meme 1"},
    {"creator": "Blake", "text": "Meme 2"}
]

print(count_meme_creators(memes))
print(count_meme_creators(memes_2))
print(count_meme_creators(memes_3))

"""
Example Output:

{'Alex': 2, 'Jordan': 2, 'Chris': 1}
{'Sam': 3, 'Taylor': 1}
{'Blake': 2}
"""