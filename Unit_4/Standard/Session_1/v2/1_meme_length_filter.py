""" 
You need to filter out memes that are too long from your dataset. Memes that exceed a certain length are less likely to go viral.

Write the filter_meme_lengths() function, which filters out memes whose lengths exceed a given limit. The function should return a list of meme texts that are within the acceptable length.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""
def filter_meme_lengths(memes, max_length):
    pass

# Example Usage:

memes = ["This is hilarious!", "A very long meme that goes on and on and on...", "Short and sweet", "Too long! Way too long!"]
memes_2 = ["Just right", "This one's too long though, sadly", "Perfect length", "A bit too wordy for a meme"]
memes_3 = ["Short", "Tiny meme", "Small but impactful", "Extremely lengthy meme that no one will read"]

print(filter_meme_lengths(memes, 20))
print(filter_meme_lengths(memes_2, 15))
print(filter_meme_lengths(memes_3, 10))

"""
Example Output:

['This is hilarious!', 'Short and sweet']
['Just right', 'Perfect length']
['Short', 'Tiny meme']
"""