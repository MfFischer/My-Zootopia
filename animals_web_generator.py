import json
import os

def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def generate_animal_info_string(animals_data):
    """Generates a string with the animals' data."""
    output = ''
    for animal in animals_data:
        output += '<li class="cards__item">\n'
        output += f"<p class='card__title'>Name: {animal.get('name')}</p>\n"
        if 'diet' in animal['characteristics']:
            output += f"<p class='card__text'>Diet: {animal['characteristics']['diet']}</p>\n"
        if 'locations' in animal and len(animal['locations']) > 0:
            output += f"<p class='card__text'>Location: {animal['locations'][0]}</p>\n"
        if 'type' in animal['characteristics']:
            output += f"<p class='card__text'>Type: {animal['characteristics']['type']}</p>\n"
        output += '</li>\n'
    return output

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

# Ensure the paths are correct
data_file_path = os.path.abspath(data_file_path)
template_file_path = os.path.abspath(template_file_path)
output_file_path = os.path.abspath(output_file_path)

# Load the data
animals_data = load_data(data_file_path)

# Generate the animal info string
animal_info_string = generate_animal_info_string(animals_data)

# Read the HTML template
template_content = read_template(template_file_path)

# Replace the placeholder with the generated animal info string
new_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animal_info_string)

# Write the new HTML content to a new file
write_html(output_file_path, new_html_content)

print(f"Generated HTML content written to {output_file_path}")
