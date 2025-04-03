"""
In your time travel adventures, you are given an integer array anomalies where anomalies[i] = [traveleri, anomalyi] indicates that the traveler traveleri caused a temporal anomaly anomalyi.

Return a list answer of size 2 where:

answer[0] is a list of all travelers that have not caused any anomalies.
answer[1] is a list of all travelers that have caused exactly one anomaly.
The values in the two lists should be returned in increasing order.

Note: You should only consider the travelers that have experienced at least one anomaly.
"""
def find_travelers(anomalies):
    pass

# Example Usage:

anomalies1 = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
anomalies2 = [[2,3],[1,3],[5,4],[6,4]]

print(find_travelers(anomalies1)) 
print(find_travelers(anomalies2))

"""
Example Output:

[[1, 2, 10], [4, 5, 7, 8]]
[[1, 2, 5, 6], []]
"""