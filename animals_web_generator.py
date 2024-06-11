import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def print_animal_details(animals_data):
    """Prints the details of each animal."""
    for animal in animals_data:
        print(f"Name: {animal.get('name')}")
        if 'diet' in animal['characteristics']:
            print(f"Diet: {animal['characteristics']['diet']}")
        if 'locations' in animal and len(animal['locations']) > 0:
            print(f"Location: {animal['locations'][0]}")
        if 'type' in animal['characteristics']:
            print(f"Type: {animal['characteristics']['type']}")
        print()

# Load the data
file_path ='animals_data.json'
animals_data = load_data(file_path)

# Print the animal details
print_animal_details(animals_data)
