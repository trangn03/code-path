""" 
You're interested in identifying groups of memes that, when combined, have a total popularity score closest to a target value. Each meme has an associated popularity score, and you want to find the two memes whose combined popularity score is closest to the target value. The list of memes is already sorted by their popularity scores.

Write the find_closest_meme_pair() function, which takes a sorted list of memes (each with a name and a popularity score) and a target popularity score. The function should return the names of the two memes whose combined popularity score is closest to the target.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""
def find_closest_meme_pair(memes, target):
    pass

# Example Usage:

memes_1 = [("Distracted boyfriend", 5), ("Dogecoin to the moon!", 7), ("One does not simply walk into Mordor", 12)]
memes_2 = [("Surprised Pikachu", 2), ("This is fine", 6), ("Expanding brain", 9), ("Y U No?", 15)]
memes_3 = [("Philosoraptor", 1), ("Bad Luck Brian", 4), ("First world problems", 8), ("Y U No?", 13)]

print(find_closest_meme_pair(memes_1, 13))
print(find_closest_meme_pair(memes_2, 10))
print(find_closest_meme_pair(memes_3, 12))

"""
Example Output:

('Distracted boyfriend', 'Dogecoin to the moon!')
('Surprised Pikachu', 'Expanding brain')
('Bad Luck Brian', 'First world problems')
"""
