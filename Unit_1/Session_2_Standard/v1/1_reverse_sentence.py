""" 
Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed. 
The sentence will contain only alphabetic characters and spaces to separate the words. 
If there is only one word in the sentence, the function should return the original string.
"""

# Split the string -> 
def reverse_sentence(sentence):
    
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence
        



sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))