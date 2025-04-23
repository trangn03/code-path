"""
You are a talented actor looking for your next big movie and want to leverage your connections to see if there are any good roles available. To increase your chances, you want to ask your closest friends first.
You have a 2D list contacts where contacts[i] = [celebrity_a, celebrity_b] indicates that there is a mutual relationship (undirected edge) between celebrity_a and celebrity_b. Given a celebrity celeb, return a list of the celebrity's closest friends.
celebrity_b is a close friend of celebrity_a if they are neighbors in the graph.
"""
def get_close_friends(contacts, celeb):
    pass

# Example Usage:

contacts = [["Lupita Nyong'o", "Jordan Peele"], ["Meryl Streep", "Jordan Peele"], ["Meryl Streep", "Lupita Nyong'o"], 
["Greta Gerwig", "Meryl Streep"], ["Ali Wong", "Greta Gergwig"]]

print(get_close_friends(contacts, "Lupita Nyong'o"))
print(get_close_friends(contacts, "Greta Gerwig"))

"""
Example Output:

['Jordan Peele', 'Meryl Streep']
['Meryl Streep', 'Ali Wong']
"""
