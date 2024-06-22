import requests

API_KEY = 'MadvaeVZ04sYTrhNCutqeQ==TfZbAInNf69NtvQr'
TEMPLATE_FILE_PATH = 'animals_template.html'
OUTPUT_FILE_PATH = 'animals.html'


def fetch_animal_data(api_key, animal_name):
    """Fetches animal data from the API Ninja Animals API."""
    url = "https://api.api-ninjas.com/v1/animals"
    headers = {'X-Api-Key': api_key}
    params = {'name': animal_name}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


def get_available_characteristics(animals_data):
    """Extracts unique characteristics from the data."""
    characteristics = set()
    for animal in animals_data:
        characteristics.update(animal.get('characteristics', {}).keys())
    return list(characteristics)


def generate_animal_info_string(animals_data):
    """Generates a string with the animals' data."""
    output = ''
    for animal in animals_data:
        output += '<li class="cards__item">\n'
        output += f"  <div class='card__title'>{animal.get('name')}</div>\n"
        output += "  <div class='card__text'>\n"
        output += "    <ul class='card__details'>\n"

        characteristics = animal.get('characteristics', {})

        for key, value in characteristics.items():
            output += (
                f"      <li class='card__detail-item'>"
                f"<strong>{key.capitalize()}:</strong> {value}"
                "</li>\n"
            )

        output += "    </ul>\n"
        output += "  </div>\n"
        output += '</li>\n'
    return output


def filter_animals_by_characteristic(animals_data, characteristic, value):
    """Filters the animals by the specified characteristic and value."""
    return [
        animal for animal in animals_data
        if animal.get('characteristics', {}).get(characteristic, '').lower() == value.lower()
    ]


def read_template(file_path):
    """Reads the HTML template file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def write_html(output_path, content):
    """Writes the content to an HTML file."""
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)


def main():
    # Get animal name from user
    animal_name = input("Enter the name of the animal you want to search for: ").strip()

    # Fetch animal data from the API
    animals_data = fetch_animal_data(API_KEY, animal_name)

    if animals_data:
        # Get available characteristics and display them to the user
        available_characteristics = get_available_characteristics(animals_data)
        print("Available characteristics:", ", ".join(available_characteristics))
        selected_characteristic = input("Enter a characteristic from the above list: ").strip()

        # Get unique values for the selected characteristic
        unique_values = set(animal['characteristics'].get(selected_characteristic, '') for animal in animals_data)
        print(f"Available values for {selected_characteristic}:", ", ".join(unique_values))
        selected_value = input(f"Enter a value for {selected_characteristic}: ").strip()

        # Filter animals by the selected characteristic and value
        filtered_animals = filter_animals_by_characteristic(animals_data, selected_characteristic, selected_value)

        if not filtered_animals:
            print(f"No animals found with {selected_characteristic} = '{selected_value}'")
        else:
            # Generate the animal info string
            animal_info_string = generate_animal_info_string(filtered_animals)

            # Read the HTML template
            template_content = read_template(TEMPLATE_FILE_PATH)

            # Replace the placeholder with the generated animal info string
            new_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animal_info_string)

            # Write the new HTML content to a new file
            write_html(OUTPUT_FILE_PATH, new_html_content)

            print(f"Generated HTML content written to {OUTPUT_FILE_PATH}")
    else:
        print("Failed to fetch animal data from the API.")


if __name__ == "__main__":
    main()
