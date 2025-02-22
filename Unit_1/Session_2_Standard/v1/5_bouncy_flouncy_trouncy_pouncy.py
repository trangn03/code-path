"""
Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations. 
"""

def final_value_after_operations(operations):
    tiger = 1
    
    for i in operations: 
        if (i == "bouncy" or i == "flouncy"):
            tiger += 1
        elif (i == "trouncy" or i == "pouncy"):
            tiger -= 1
    return tiger


operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

""" 
Example Output:

2
4
"""