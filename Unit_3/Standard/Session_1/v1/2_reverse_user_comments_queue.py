"""
On your platform, comments on posts are displayed in the order they are received. 
However, for a special feature, you need to reverse the order of comments before displaying them. 
Given a queue of comments represented as a list of strings, reverse the order using a stack. 
"""

def reverse_comments_queue(comments):
  # Have an empty stack to store the comment
  # Go through each comments and add to the temp stack 
  stack = []
  for i in comments:
    stack.append(i)
    
  reverse_cmt = []
  # Pop elements from the stack one by one, 
  # appending each to the reversed comments list.
  while stack:
    take_out = stack.pop()
    reverse_cmt.append(take_out)
  
  return reverse_cmt
    
  

# Example Usage:

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

"""
Example Output:

['Thanks for sharing.', 'Love it!', 'Great post!']
['Well written.', 'Interesting read.', 'First!']
"""