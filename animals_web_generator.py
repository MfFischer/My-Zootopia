import json

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def get_available_skin_types(animals_data):
    """Extracts unique skin_type values from the data."""
    skin_types = set()
    for animal in animals_data:
        skin_type = animal['characteristics'].get('skin_type')
        if skin_type:
            skin_types.add(skin_type)
    return list(skin_types)

def generate_animal_info_string(animals_data):
    """Generates a string with the animals' data."""
    output = ''
    for animal in animals_data:
        output += '<li class="cards__item">\n'
        output += f"  <div class='card__title'>{animal.get('name')}</div>\n"
        output += f"  <div class='card__text'>\n"
        output += "    <ul class='card__details'>\n"
        if 'locations' in animal and len(animal['locations']) > 0:
            output += f"      <li class='card__detail-item'><strong>Location:</strong> {animal['locations'][0]}</li>\n"
        if 'type' in animal['characteristics']:
            output += f"      <li class='card__detail-item'><strong>Type:</strong> {animal['characteristics']['type']}</li>\n"
        if 'diet' in animal['characteristics']:
            output += f"      <li class='card__detail-item'><strong>Diet:</strong> {animal['characteristics']['diet']}</li>\n"
        if 'lifespan' in animal['characteristics']:
            output += f"      <li class='card__detail-item'><strong>Lifespan:</strong> {animal['characteristics']['lifespan']}</li>\n"
        if 'weight' in animal['characteristics']:
            output += f"      <li class='card__detail-item'><strong>Weight:</strong> {animal['characteristics']['weight']}</li>\n"
        if 'length' in animal['characteristics']:
            output += f"      <li class='card__detail-item'><strong>Length:</strong> {animal['characteristics']['length']}</li>\n"
        output += "    </ul>\n"
        output += f"  </div>\n"
        output += '</li>\n'
    return output

def filter_animals_by_skin_type(animals_data, skin_type):
    """Filters the animals by the specified skin_type."""
    return [animal for animal in animals_data if animal['characteristics'].get('skin_type') == skin_type]

def read_template(file_path):
    """Reads the HTML template file."""
    with open(file_path, "r") as file:
        return file.read()

def write_html(output_path, content):
    """Writes the content to an HTML file."""
    with open(output_path, "w") as file:
        file.write(content)

# Define the paths to the data and template files
data_file_path = 'animals_data.json'
template_file_path = 'animals_template.html'
output_file_path = 'animals.html'

# Load the data
animals_data = load_data(data_file_path)

# Get available skin types and display them to the user
available_skin_types = get_available_skin_types(animals_data)
print("Available skin types:", ", ".join(available_skin_types))
selected_skin_type = input("Enter a skin type from the above list: ").strip()

# Filter animals by the selected skin type
filtered_animals = filter_animals_by_skin_type(animals_data, selected_skin_type)

if not filtered_animals:
    print(f"No animals found with skin type '{selected_skin_type}'")
else:
    # Generate the animal info string
    animal_info_string = generate_animal_info_string(filtered_animals)

    # Read the HTML template
    template_content = read_template(template_file_path)

    # Replace the placeholder with the generated animal info string
    new_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animal_info_string)

    # Write the new HTML content to a new file
    write_html(output_file_path, new_html_content)

    print(f"Generated HTML content written to {output_file_path}")
