"""
Imagine you are working on a wildlife conservation database. Write a function named most_endangered() that returns the species with the highest conservation priority based on its population.

The function should take in a list of dictionaries named species_list as a parameter. Each dictionary represents data associated with a species, including its name, habitat, and wild population. The function should return the name of the species with the lowest population.

If there are multiple species with the lowest population, return the species with the lowest index. 
"""

def most_endangered(species_list):
    # Initialize the most endangered species
    most_endangered_species = species_list[0]
    # Iterate through the list of spcies
    for species in species_list[1:]:
    # If the current species has lower population than the current most endangered
        if species["population"] < most_endangered_species["population"]:
            most_endangered_species = species
    # Return the name of the most endangered species
    return most_endangered_species["name"]

# Example Usage:

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list)) # Vaquita