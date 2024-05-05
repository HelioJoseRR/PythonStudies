favorite_places = {
    'carla': ['paris', 'new york', 'tokyo'],
    'joseph': ['london', 'rome', 'barcelona'],
    'michael': ['dubai', 'singapore', 'sydney'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")