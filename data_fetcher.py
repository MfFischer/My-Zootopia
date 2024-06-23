import requests

API_KEY = 'MadvaeVZ04sYTrhNCutqeQ==TfZbAInNf69NtvQr'

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    """
    url = "https://api.api-ninjas.com/v1/animals"
    headers = {'X-Api-Key': API_KEY}
    params = {'name': animal_name}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None
