destionations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brasil", "Cairo, Egypt"];
test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical sites", "art"]]

def get_destination_index(destination):
    return destionations.index(destination);

def get_traveler_location(traveler):
    traveler_destination = traveler[1];
    return get_destination_index(traveler_destination);

test_destination_index = get_traveler_location(test_traveler);

print(test_destination_index);