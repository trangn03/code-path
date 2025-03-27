""" 
You've been given partially completed code to identify pairs of memes that frequently appear together in posts. However, before you can complete the implementation, you need to ensure the plan is correct and then review the provided code to identify and fix any potential issues.

Your task is to:

Plan:

Write a detailed plan (pseudocode or step-by-step instructions) on how you would approach solving this problem. Consider how you would:

Iterate through each post.

Generate pairs of memes.

Count the frequency of each pair.

Identify pairs that appear more than once.

Ensure the final result is accurate and efficient.

Review:

Examine the provided code and answer the following questions:

Are there any logical errors in the code? If so, what are they, and how would you fix them?

Are there any inefficiencies in the code that could be improved? If so, how would you optimize it?

Does the code correctly handle edge cases, such as an empty list of posts or posts with only one meme?
"""

def find_trending_meme_pairs(meme_posts):
    pair_count = {}

    for post in meme_posts:
        for i in range(len(post)):
            for j in range(len(post)):
                if i != j:
                    meme1 = post[i]
                    meme2 = post[j]

                    if meme1 < meme2:
                        meme1, meme2 = meme2, meme1
                    pair = (meme1, meme2)
                    if pair in pair_count:
                        pair_count[pair] += 1
                    else:
                        pair_count[pair] = 1

    trending_pairs = []
    for pair in pair_count:
        if pair_count[pair] >= 2:
            trending_pairs.append(pair)

    return trending_pairs

# Example Usage:

meme_posts_1 = [
    ["Dogecoin to the moon!", "Distracted boyfriend"],
    ["One does not simply walk into Mordor", "Dogecoin to the moon!"],
    ["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"],
    ["Distracted boyfriend", "One does not simply walk into Mordor"]
]

meme_posts_2 = [
    ["Surprised Pikachu", "This is fine"],
    ["Expanding brain", "Surprised Pikachu"],
    ["This is fine", "Expanding brain"],
    ["Surprised Pikachu", "This is fine"]
]

meme_posts_3 = [
    ["Y U No?", "First world problems"],
    ["Philosoraptor", "Bad Luck Brian"],
    ["First world problems", "Philosoraptor"],
    ["Y U No?", "First world problems"]
]

print(find_trending_meme_pairs(meme_posts))
print(find_trending_meme_pairs(meme_posts_2))
print(find_trending_meme_pairs(meme_posts_3))

"""
Example Output:

[('Distracted boyfriend', 'Dogecoin to the moon!'), ('Dogecoin to the moon!', 'One does not simply walk into Mordor'), ('Distracted boyfriend', 'One does not simply walk into Mordor')]
[('Surprised Pikachu', 'This is fine')]
[('First world problems', 'Y U No?')]
"""