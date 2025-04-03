""" 
As a digital nomad who frequently writes and edits HTML for your blog, you want to ensure that your HTML code is properly structured. One important aspect of HTML structure is ensuring that all opening tags have corresponding closing tags and that they are properly nested.

Given a string of HTML-like tags (simplified for this problem), write a function to determine if the tags are properly nested and closed. The tags will be in the form of <tag> for opening tags and </tag> for closing tags.

The function should return True if the tags are properly nested and closed, and False otherwise.

Assumptions:

You can assume that tags are well-formed (e.g., <div>, </div>, <a>, </a>, etc.).

Tags can be nested but cannot overlap improperly (e.g., <div><p></div></p> is invalid).

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

def validate_html_tags(html):
  pass

# Example Usage:

html = "<div><p></p></div>"
print(validate_html_tags(html))

html_2 = "<div><p></div></p>"
print(validate_html_tags(html_2))

html_3 = "<div><p><a></a></p></div>"
print(validate_html_tags(html_3))

html_4 = "<div><p></a></p></div>"
print(validate_html_tags(html_4))

"""
Example Output:

True
False
True
False
"""