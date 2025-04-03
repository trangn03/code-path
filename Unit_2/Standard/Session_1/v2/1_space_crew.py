"""
Given two lists of length n, crew and position, map the space station crew to their position on board the international space station.
Each crew member crew[i] has job position[i] on board, where 0 <= i < n and len(crew) == len(position).
Hint: Introduction to dictionaries 
"""

def space_crew(crew, position):
    pass
# Example Usage:

exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", " Flight Engineer", "Flight Engineer"] 

ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]

print(space_crew(exp70_crew, exp70_positions))
print(space_crew(ax3_crew, ax3_positions))

"""
Example Output:

{
    "Andreas Mogensen": "Commander",
    "Jasmin Moghbeli": "Flight Engineer",
    "Satoshi Furukawa": "Flight Engineer",
    "Loral O'Hara": "Flight Engineer",
    "Konstantin Borisov": "Flight Engineer",
}

{
    "Michael López-Alegría": "Commander",
    "Walter Villadei": "Mission Pilot",
    "Alper Gezeravcı": "Mission Specialist",
    "Marcus Wandt": "Mission Specialist"
}
"""