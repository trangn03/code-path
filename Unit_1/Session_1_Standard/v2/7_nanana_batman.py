"""
Write a function nanana_batman() that accepts an integer x 
and prints the string "nanana batman!" where "na" is repeated x times. 
Do not use the * operator. 
"""

def nanana_batman(x):
    str = ""
    for i in range(x):
        str += "na"
    result = str + " batman"
    
    print(result)
        

# Example Usage
x = 6
nanana_batman(x)

x = 0
nanana_batman(x)


# Example Output:
""" 
"nananananana batman!"
"batman!"
"""
