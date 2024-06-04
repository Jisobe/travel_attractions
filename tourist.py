destionations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"];
attractions = [[], [], [], [], []]
test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical sites", "art"]]

def get_destination_index(destination):
    return destionations.index(destination);

def get_traveler_location(traveler):
    traveler_destination = traveler[1];
    return get_destination_index(traveler_destination);

def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination);
    attractions[destination_index].append(attraction);
    return;

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']]);
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
print(attractions);