def average_nft_value(nft_collection):
    # Return 0
    if not nft_collection:
        return 0
    
    # Calculate the total value
    # Iterate through each nft in collection
    # Add the value
    total_value = 0
    for nft in nft_collection:
        total_value += nft["value"]
    ave_value = total_value / len(nft_collection)
    return ave_value

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))