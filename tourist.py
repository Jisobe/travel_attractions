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

def find_attraction(destination, interests):
    destination_index = get_destination_index(destination);
    attractions_in_city = attractions[destination_index];
    attractions_with_interest = [];

    for attraction in attractions_in_city:
        for interest in interests:
            if interest in attraction[1]:
                attractions_with_interest.append(attraction[0]);
            
    return attractions_with_interest;

def get_attractions_for_traveler(traveler):
    traveler_name = traveler[0];
    traveler_dest = traveler[1];
    traveler_interests = traveler[2];

    traveler_attractions = find_attraction(traveler_dest, traveler_interests);

    output_string = f"Hi {traveler[0]}, we think you'll like these places around {traveler_dest}:\n"

    for attraction in traveler_attractions:
        output_string += "-" + attraction + "\n";
    
    # output_string += (str(attraction) for attraction in traveler_attractions);

    return output_string;


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

print(get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']]))