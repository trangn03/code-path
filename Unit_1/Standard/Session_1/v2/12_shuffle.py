"""
Write a function shuffle() that accepts a list cards of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. 
Return the list in the form [x1,y1,x2,y2,...,xn,yn]. 
"""

def shuffle(cards):
    # Initialize new list 
    list = [] 
    # Calculate n as half length of the list 
    n = len(cards) // 2
    for i in range(n):
        list.append(cards[i])
        list.append(cards[i+n])
    return list

#Example Usage

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
print(shuffle(cards))

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
print(shuffle(cards))

cards = [10, 10, 2, 2]
print(shuffle(cards))

# Example Output:
"""
['Joker', 3, 'Queen', 'Ace', 2, 7]
[9, 'Joker', 2, 3, 3, 2, 'Joker', 9]
[10, 2, 10, 2]
"""