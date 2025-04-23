""" 
You work for a talent agency and have a 2D list clients where clients[i] = [celebrity_a, celebrity_b] indicates that celebrity_a and celebrity_b have worked with each other. You want to create a more efficient lookup system for your agency by transforming clients into an equivalent adjacency matrix.

Given contacts:

Create a map of each unique celebrity in contacts to an integer ID with values 0 through n.
Using the celebrities' IDs, create an adjacency matrix where matrix[i][j] = 1 indicates that celebrity with ID i has worked with celebrity with ID j. Otherwise, matrix[i][j] should have value 0.
Return both the dictionary mapping celebrities to their ID and the adjacency matrix.
"""

def get_adj_matrix(clients):
    pass

clients = [
            ["Yalitza Aparicio", "Julio Torres"], 
            ["Julio Torres", "Fred Armisen"], 
            ["Bowen Yang", "Julio Torres"],
            ["Bowen Yang", "Margaret Cho"],
            ["Margaret Cho", "Ali Wong"],
            ["Ali Wong", "Fred Armisen"], 
            ["Ali Wong", "Bowen Yang"]]

id_map, adj_matrix = get_adj_matrix(clients)
print(id_map)
print(adj_matrix)


"""
Example Output:

{
  'Fred Armisen': 0,
  'Yalitza Aparicio': 1,
  'Margaret Cho': 2,
  'Bowen Yang': 3,
  'Ali Wong': 4,
  'Julio Torres': 5
}

[
  [0, 0, 0, 0, 1, 1],  # Fred Armisen
  [0, 0, 0, 0, 0, 1],  # Yalitza Aparicio
  [0, 0, 0, 1, 1, 0],  # Margaret Cho
  [0, 0, 1, 0, 1, 1],  # Bowen Yang
  [1, 0, 1, 1, 0, 0],  # Ali Wong
  [1, 1, 0, 1, 0, 0]   # Julio Torres
]

Note: The order in which you assign IDs and consequently your adjacency matrix may look different
"""