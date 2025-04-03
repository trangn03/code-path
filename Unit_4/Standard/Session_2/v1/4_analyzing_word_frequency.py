""" 
As a digital nomad who writes blogs, articles, and reports regularly, it's important to analyze the text you produce to ensure clarity and avoid overusing certain words. You want to create a tool that analyzes the frequency of each word in a given text and identifies the most frequent word(s).

Given a string of text, write a function that returns the unique words and the number of times each word appears in the text. Additionally, return a list of the word(s) that appear most frequently.

Assumptions:

The text is case-insensitive, so "Word" and "word" should be treated as the same word.

Punctuation should be ignored.

In case of a tie, return all words that have the highest frequency.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

def word_frequency_analysis(text):
  pass

# Example Usage:

text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
print(word_frequency_analysis(text))

text_2 = "Digital nomads love to travel. Travel is their passion."
print(word_frequency_analysis(text_2))

text_3 = "Stay connected. Stay productive. Stay happy."
print(word_frequency_analysis(text_3))

"""
Example Output:

({'the': 3, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 2, 'was': 1, 'not': 1, 'amused': 1}, ['the'])
({'digital': 1, 'nomads': 1, 'love': 1, 'to': 1, 'travel': 2, 'is': 1, 'their': 1, 'passion': 1}, ['travel'])
({'stay': 3, 'connected': 1, 'productive': 1, 'happy': 1}, ['stay'])
"""