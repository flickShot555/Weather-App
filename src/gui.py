import tkinter as tk
from weather_api import get_weather_data

def fetch_weather():
    lat, lon = lat_entry.get(), lon_entry.get()
    weather = get_weather_data(lat, lon)
    
    if "error" in weather:
        result_label.config(text="Error fetching data")
    else:
        result_label.config(text=f"Temp: {weather['temperature']}°C\nWind: {weather['windspeed']} km/h")

# GUI Setup
root = tk.Tk()
root.title("Weather App")

tk.Label(root, text="Latitude:").pack()
lat_entry = tk.Entry(root)
lat_entry.pack()

tk.Label(root, text="Longitude:").pack()
lon_entry = tk.Entry(root)
lon_entry.pack()

fetch_button = tk.Button(root, text="Get Weather", command=fetch_weather)
fetch_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
