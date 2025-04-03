""" 
If you implemented find_common_signals() in the previous problem using dictionaries, try implementing find_common_signals() again using sets instead of dictionaries. 
If you implemented find_common_signals() using sets, use dictionaries this time.
Once you've come up with your second solution, compare the two. Is one solution better than the other? How so? Why or why not?
"""

def find_common_signals(signals1, signals2):
    pass
# Example Usage:

signals1_example1 = [2, 3, 2]
signals2_example1 = [1, 2]
print(find_common_signals(signals1_example1, signals2_example1))

signals1_example2 = [4, 3, 2, 3, 1]
signals2_example2 = [2, 2, 5, 2, 3, 6]
print(find_common_signals(signals1_example2, signals2_example2))

signals1_example3 = [3, 4, 2, 3]
signals2_example3 = [1, 5]
print(find_common_signals(signals1_example3, signals2_example3))

# Example Output:

# [2, 1]
# [3, 4]
# [0, 0]