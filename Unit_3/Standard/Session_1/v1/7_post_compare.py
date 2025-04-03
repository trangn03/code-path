""" 
You often draft your posts and edit them before publishing. 
Given two draft strings draft1 and draft2, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will remain empty.
"""
# Helper function
def build_final_string(draft):
  # Initialize empty stack
  stack = []
  # Iterate through each character in the draft 
  # If the char is "#", pop the top char 
  # Otherwise, push the character onto the stack.
  for char in draft:
    if char == "#":
      if stack:
        stack.pop()
    else:
      stack.append(char)
  return stack 

def post_compare(draft1, draft2):
  final_draft1 = build_final_string(draft1)
  final_draft2 = build_final_string(draft2)
  
  return final_draft1 == final_draft2


# Example Usage:

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 

"""
Example Output:

True
True
False
"""