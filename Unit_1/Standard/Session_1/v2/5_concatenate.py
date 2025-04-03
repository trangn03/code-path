"""
Write a function concatenate() that takes in a list of strings words 
and returns a string concatenated that concatenates all elements in words. 
"""

def concatenate(words):
    w = ""
    for i in words:
        w += i
    return w


words = ["vengeance", "darkness", "batman"]
print(concatenate(words))

words = []
print(concatenate(words))