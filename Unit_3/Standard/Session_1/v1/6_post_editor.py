""" 
You want to add a creative twist to your posts by reversing the order of characters in each word within your post 
while still preserving whitespace and the initial word order. 
Given a string post, use a queue to reverse the order of characters in each word within the sentence.
"""
# Queue problem 
from collections import deque

def edit_post(post):
  # Empty list to build final result
  result = []
  # Empty deque to hold the characters 
  queue = deque()
  
  # Initialize through each character in the post
  # If char is not a space, enqueue it to the queue
  for char in post:
    if char != ' ':
      queue.append(char) # Enqueue character
    # If char is a space, dequeue all characters from deque (which reverses the word) 
    # and append them to the result list. 
    # Then append the space to the result list.
    else:
      while queue:
        result.append(queue.pop())
      result.append(' ')
  # After the loop, handle any remaining characters in the deque
  while queue:
    result.append(queue.pop())
  
  # Join all elements in the result list to form the final string and return it
  return ''.join(result)

# Example Usage:

print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 

"""
Example Output:

tsooB ruoy tnemegegna htiw esehT spit
kcehC tuo ym tseval golv
"""