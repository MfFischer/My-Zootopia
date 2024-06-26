import data_fetcher

TEMPLATE_FILE_PATH = 'animals_template.html'
OUTPUT_FILE_PATH = 'animals.html'


def generate_animal_info_string(animals_data, animal_name):
    """Generates a string with the animals' data or an error message if no data found."""
    if not animals_data:
        return (
            f'<h2>The animal "<span style="color:red;">'
            f'{animal_name}'
            f'</span>" doesn\'t exist.</h2>'
        )

    output = ''
    for animal in animals_data:
        output += '<li class="cards__item">\n'
        output += f" <div class='card__title'>{animal.get('name')}</div>\n"
        output += "  <div class='card__text'>\n"
        output += "  <ul class='card__details'>\n"

        characteristics = animal.get('characteristics', {})

        for key, value in characteristics.items():
            output += (
                f"<li class='card__detail-item'>"
                f"<strong>{key.capitalize()}:</strong> {value}"
                "</li>\n"
            )

        output += "    </ul>\n"
        output += "  </div>\n"
        output += '</li>\n'
    return output


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
    animal_name = input("Enter a name of an animal: ").strip()

    # Fetch animal data using the data_fetcher module
    animals_data = data_fetcher.fetch_data(animal_name)

    # Generate the animal info string or error message
    animal_info_string = generate_animal_info_string(animals_data, animal_name)

    # Read the HTML template
    template_content = read_template(TEMPLATE_FILE_PATH)

    # Replace the placeholder with animal info string or error message
    new_html_content = template_content.replace('__REPLACE_ANIMALS_INFO__', animal_info_string)

    # Write the new HTML content to a new file
    write_html(OUTPUT_FILE_PATH, new_html_content)

    print(f"Website was successfully generated to the file {OUTPUT_FILE_PATH}.")


if __name__ == "__main__":
    main()
