""" 
Write a function sum_of_digits() that accepts an integer num and returns the sum of num's digits.
"""

def sum_of_digits(num):
    total = 0
    
    while num > 0:
        total += num %10 # modulo gives the remainder 
        num //= 10
    return total 


num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))

num = 4687
print(sum_of_digits(num))

"""
Example Output:
9 # Explanation: 4 + 2 + 3 = 9
4 
25 
"""