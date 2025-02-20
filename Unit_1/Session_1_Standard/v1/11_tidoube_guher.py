""" 
Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. 
Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g, e, and r from it.
"""

def tiggerfy(s):
    result = ""
    
    for letter in s:
        if letter.lower() not in "tiger":
            result += letter
    return result


s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))