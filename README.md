# 🌦️ Weather App

A simple Python-based Weather App that fetches real-time weather data using OpenWeatherMap API. It includes a CLI version, a GUI using Tkinter, and a Flask-based web interface.

## 🚀 Features
- 🌍 Fetches real-time weather data.
- 🖥️ Command Line Interface (CLI).
- 🖼️ Graphical User Interface (GUI) with Tkinter.
- 🌐 Web-based version using Flask.
- 🛠️ Simple and easy-to-use design.

## 📂 Project Structure
weather_app/ 

│── venv/               # Virtual environment

│── src/                # Source code

│ ├── main.py           # CLI version

│ ├── gui.py            # Tkinter GUI version

│ ├── webapp.py         # Flask web version

│ ├── weather_api.py    # API call module

│── templates/          # HTML templates

│── requirements.txt    # Dependencies

│── README.md           # Documentation

│── .gitignore          # Ignore unnecessary files


## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/flickShot555/weather-app.git
   cd weather-app

   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   pip install -r requirements.txt

   running CLI Version:
   python src/main.py

   running GUI Version:
   python src/gui.py

   running Web version
   python src/webapp.py

🌍 API Key Setup
    This app uses OpenWeatherMap API. Get your free API key from OpenWeatherMap and replace 'your_api_key_here' in 'weather_api.py'.

📜 License
    This project is licensed under the MIT License.

📬 Contact
    Created by Abbas Khan
    www.aepostrophee.kesug.com
    
    – Feel free to reach out!

