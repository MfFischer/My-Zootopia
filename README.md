# 🦊 My Zootopia Project 🐾

Welcome to the **My Zootopia Project**! This project allows you to fetch detailed information about various animals and generate a user-friendly HTML website displaying this information.

## ✨ Features

- 📚 **Fetch Animal Data**: Get detailed information about any animal using the API Ninjas.
- 🌐 **Generate HTML**: Create a visually appealing HTML page with the fetched data.
- 🔄 **Flexible Data Fetching**: Easily switch between different data sources by modifying the `data_fetcher.py` file.
- 🔒 **Secure API Key Management**: Use environment variables to securely manage your API key.

## ⚙️ Setup and Installation

### Prerequisites

- Python 3.x
- `pip` package manager

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MfFischer/My-Zootopia.git
   cd My-Zootopia
2. **Create and Activate a Virtual Environment** (Optional but Recommended):
   ```bash 
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Create a .env File**:
   In the root directory, create a file named '.env' and add your API key:
   ```plaintext
   API_KEY='your_api_key_here'

### 🚀 Usage

1.  **Run the Application**:
      ```bash
      python animals_web_generator.py
      
2. **Enter an Animal Name**:
  
     When prompted, enter the name of the animal you want information about (e.g., "Fox").
   
3. **View the Generated Website**:

   The application will generate an animals.html file in the root directory.

   Open this file in your web browser to view the animal information.

### 🤝 Contributing

    Contributions are welcome! Please follow these steps to contribute:

      1. Fork the repository.
  	  2. Create a new branch (git checkout -b feature-branch).
      3. Make your changes.
      4. Commit your changes (git commit -m 'Add some feature').
      5. Push to the branch (git push origin feature-branch).
      6. Open a pull request.

### 🙏 Acknowledgements

      Thanks to API Ninjas for providing the animal data API.
